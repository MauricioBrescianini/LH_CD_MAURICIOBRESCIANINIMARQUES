import pandas as pd
import numpy
import seaborn as sns
import matplotlib.pyplot as plt

# ajustar dados
def predefinicao(filepath):
    df = pd.read_csv(filepath)
    df['Runtime'] = df['Runtime'].str.replace(' min', '').astype(int)
    df['Gross'] = df['Gross'].str.replace(',', '').astype(float)
    df['Nota_arredondada'] = numpy.ceil(df['Meta_score'] / 10).clip(upper=10)
    df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')
    df['Meta_score'] = pd.to_numeric(df['Meta_score'], errors='coerce')
    df['Main_Genre'] = df['Genre'].str.split(',').str[0]
    return df

def top_atores(df):
    #concatena as colunas de atores
    df_atores = pd.concat([df['Star1'], df['Star2'], df['Star3'], df['Star4']])
    top_atores = df_atores.value_counts().head(9)
    
    # Geração do Gráfico
    plt.style.use('classic')
    plt.figure(figsize=(12, 8))
    sns.barplot(x=top_atores.values, y=top_atores.index, hue=top_atores.index, palette='plasma', legend=False)
    plt.title('Top 9 Atores por Número de Filmes', fontsize=18, fontweight='bold')
    plt.xlabel('Número de Filmes', fontsize=14)
    plt.ylabel('Ator', fontsize=14)
    plt.tight_layout()
    plt.show

def distribuicao_ano_lancamento(df):
    # filtrar
    df_anos = df[df['Released_Year'] >= 2000].copy()

    # agrupar
    bins = range(2000, int(df_anos['Released_Year'].max()) + 2, 2)
    labels = [f'{i}-{i+1}' for i in bins[:-1]]
    df_anos['Faixa_Anos'] = pd.cut(df_anos['Released_Year'], bins=bins, labels=labels, right=False)
    
    filmes_por_faixa = df_anos['Faixa_Anos'].value_counts().sort_index()

    # grafico
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 6))
    sns.barplot(x=filmes_por_faixa.index, y=filmes_por_faixa.values, color='cadetblue')
    plt.title('Distribuição de Lançamentos por Ano (a partir de 2000)', fontsize=16, fontweight='bold')
    plt.xlabel('Faixa de Anos', fontsize=12)
    plt.ylabel('Quantidade de Filmes', fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show

def metricas_diretores(df):
    # tratamento
    df['Gross'] = df['Gross'].astype(str).str.replace(',', '').astype(float)
    df['Gross'] = df['Gross'].fillna(df['Gross'].mean())
    
    # top 10 diretores com mais filmes e receita total
    contagem_diretores = df['Director'].value_counts().head(10)
    top_10_diretores = contagem_diretores.index.tolist()
    arrecadacao_total_diretores = df[df['Director'].isin(top_10_diretores)].groupby('Director')['Gross'].sum()
    
    # grafico
    fig, ax1 = plt.subplots(figsize=(14, 7))
    fig.suptitle('Número de Filmes e Arrecadação Total dos Top 10 Diretores', fontsize=16, fontweight='bold')

    # primeiro eixo = contagem filmes
    sns.barplot(x=contagem_diretores.values, y=contagem_diretores.index, ax=ax1, color='skyblue')
    ax1.set_xlabel('Número de Filmes', color='skyblue')
    ax1.tick_params(axis='x', colors='skyblue')
    
    # segundo eixo = arrecadação total
    ax2 = ax1.twiny()
    sns.barplot(x=arrecadacao_total_diretores.values, y=arrecadacao_total_diretores.index, ax=ax2, color='coral')
    ax2.tick_params(axis='x', colors='coral')
    ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: f'${x/1e9:.2f}B'))

    plt.style.use('seaborn-v0_8-bright')
    plt.tight_layout()
    plt.show()

def filmes_populares(df):
    # filtro
    df_popular = df.dropna(subset=['No_of_Votes', 'Gross', 'Meta_score']).copy()
    
    # metricas para escala 0 a 1
    metricas = ['No_of_Votes', 'Gross', 'Meta_score']
    for col in metricas:
        min_val = df_popular[col].min()
        max_val = df_popular[col].max()
        df_popular[f'{col}_norm'] = (df_popular[col] - min_val) / (max_val - min_val)

    # calcula popularidade
    norm_cols = [f'{c}_norm' for c in metricas]
    df_popular['Pontuacao_Popularidade'] = df_popular[norm_cols].mean(axis=1)

    top_15_filmes = df_popular.sort_values(by='Pontuacao_Popularidade', ascending=False).head(15)
    top_15_filmes['Label_Grafico'] = top_15_filmes['Series_Title'] + '\n(' + top_15_filmes['Genre'] + ')'

    # grafico
    plt.style.use('seaborn-v0_8-darkgrid')
    plt.figure(figsize=(12, 10))
    ax = sns.barplot(
        x='Pontuacao_Popularidade', 
        y='Label_Grafico', 
        data=top_15_filmes, 
        hue='Label_Grafico', 
        palette='viridis', 
        legend=False
    )
    ax.set_xlabel('Pontuação de Popularidade', fontsize=14)
    ax.set_ylabel('Filme (Gênero)', fontsize=14)
    ax.set_title('Top 15 Filmes Mais Populares', fontsize=18, fontweight='bold')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    df = predefinicao('desafio_indicium_imdb.csv')
    top_atores(df)
    distribuicao_ano_lancamento(df)
    metricas_diretores(df)
    filmes_populares(df)