import pandas as pd
import numpy as np
import re
import joblib
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# conversoes
def converte_runtime(runtime):
    if isinstance(runtime, str):
        match = re.match(r'(\d+)', runtime)
        if match:
            return int(match.group(1))
    return np.nan

def converte_gross(gross):
    if pd.isna(gross) or (isinstance(gross, str) and gross.strip() == ''):
        return np.nan
    return float(str(gross).replace(',', '').strip())

# carregar dados
def carrega_data(caminho):
    df_filmes = pd.read_csv(caminho)
    df_filmes['Runtime'] = df_filmes['Runtime'].apply(converte_runtime)
    df_filmes['Gross'] = df_filmes['Gross'].apply(converte_gross)
    df_filmes = df_filmes.dropna(subset=['IMDB_Rating'])

    alvo = 'IMDB_Rating'
    caracteristicas = ['Released_Year', 'Runtime', 'Meta_score', 'No_of_Votes', 'Gross',
                'Certificate', 'Genre', 'Director', 'Star1', 'Star2', 'Star3', 'Star4']

    X = df_filmes[caracteristicas]
    y = df_filmes[alvo]

    colunas_num = ['Released_Year', 'Runtime', 'Meta_score', 'No_of_Votes', 'Gross']
    colunas_cat = ['Certificate', 'Genre', 'Director', 'Star1', 'Star2', 'Star3', 'Star4']

    for col in colunas_num:
        X.loc[:, col] = pd.to_numeric(X[col], errors='coerce')

    return X, y, colunas_num, colunas_cat

# criar modelo
def cria_pipeline(versao, colunas_num, colunas_cat):
    transformador_numerico = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median'))
    ])

    transformador_categorico = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])

    preprocessor = ColumnTransformer(transformers=[
        ('num', transformador_numerico, colunas_num),
        ('cat', transformador_categorico, colunas_cat)
    ])

    #modelos de regressao
    if versao == 'linear':
        regressor = LinearRegression()
    elif versao == 'random_forest':
        regressor = RandomForestRegressor(n_estimators=100, random_state=42)
    else:
        raise ValueError("Escolha 'linear' ou 'random_forest'.")

    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', regressor)
    ])

    return model

# treinar e avaliar modelo
def treinar_avaliar(model, X, y):
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_val)

    mse = mean_squared_error(y_val, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_val, y_pred)

    print(f'RMSE: {rmse:.3f}')
    print(f'R²: {r2:.3f}')
    return model

# prever nota imdb
def previsao_nota_imdb(model):
    info_filme = {
        'Released_Year': 1994,
        'Runtime': 142,
        'Meta_score': 80,
        'No_of_Votes': 2000000,
        'Gross': 28341469,
        'Certificate': 'R',
        'Genre': 'Drama',
        'Director': 'Frank Darabont',
        'Star1': 'Tim Robbins',
        'Star2': 'Morgan Freeman',
        'Star3': 'Bob Gunton',
        'Star4': 'William Sadler'
    }
    df = pd.DataFrame([info_filme])
    nota = model.predict(df)[0]
    print(f'Previsao de nota para: The Shawshank Redemption: {nota:.2f}')

if __name__ == "__main__":
    caminho = 'desafio_indicium_imdb.csv'
    X, y, colunas_num, colunas_cat = carrega_data(caminho)

    # Setar modelos: 'linear' para regressão linear e 'random_forest'
    modelo_versao = 'linear'

    model = cria_pipeline(modelo_versao, colunas_num, colunas_cat)
    modelo_treinado = treinar_avaliar(model, X, y)
    previsao_nota_imdb(modelo_treinado)

    joblib.dump(modelo_treinado, 'modelo_treinado.pkl')
    print("\n'modelo_treinado.pkl' criado com sucesso'")
