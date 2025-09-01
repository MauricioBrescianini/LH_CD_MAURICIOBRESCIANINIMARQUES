Análise e Previsão da Nota de Filmes IMDb

Este projeto realiza uma análise exploratória de dados de filmes e desenvolve um modelo de machine learning para prever a nota de um filme no IMDb, com base em suas características.

0. Configuração do Ambiente

Siga os passos abaixo para configurar o ambiente virtual e instalar as dependências necessárias:

Crie o ambiente virtual:

    python -m venv .venv

Ative o ambiente virtual:

    .venv\Scripts\Activate.ps1

Instale as bibliotecas a partir de requirements.txt:

    pip install -r requirements.txt

1. Análise Exploratória de Dados

    Execute o arquivo relatorios.py para gerar os gráficos e análises exploratórias.

    Top 9 atores com mais filmes: relatorios-imagens\top9atores.png

    Lançamentos por ano: relatorios-imagens\lancamentos_por_ano.png

    Top 10 Diretores com mais filmes e arrecadação: relatorios-imagens\top10_diretores_filmes_arrecadacao.png

    Top 15 filmes mais populares: relatorios-imagens\top15_filmes_populares.png

2. Resultados da Análise:

    2a: O filme que eu recomendaria, com base nos atributos: No_of_Votes, Gross, Meta_score, Genre e Director, seria The Dark Knight, além de realmente ser um ótimo filme

    2b: Variáveis Relevantes: As variáveis que mais influenciam a popularidade e faturamento de um filme são:

            Número de Votos (No_of_Votes): Popularidade do filme

            Gênero (Genre): Ação, aventura e drama são os gêneros mais famosos e que estão ligados aos maiores faturamentos.

            Diretor e Atores (Director, Star1, Star2...): Artistas renomados geralmente estão relacionados a filmes de alto faturamento.

            Metascore (Meta_score): Notas altas muitas vezes estão associadas a alto faturamento.

    2c: A sinopse (Overview) de um filme, na maioria dos casos, pode ser usada para descobrir seu gênero. Usando uma IA com NLP é uma boa tática para inferir o gênero de um filme com base na sinopse.

3. Modelagem Preditiva

Variáveis e Transformações Utilizadas

O modelo utiliza as seguintes variáveis para prever a nota no IMDb (IMDB_Rating):

    Numéricas: 'Released_Year', 'Runtime', 'Meta_score', 'No_of_Votes', 'Gross'.

    Categóricas: 'Certificate', 'Genre', 'Director', 'Star1', 'Star2', 'Star3', 'Star4'.

As transformações aplicadas foram:

    As colunas 'Runtime' e 'Gross' foram convertidas para o tipo numérico, removendo caracteres de texto.

    Valores nulos foram preenchidos para garantir que o modelo possa ser treinado com êxito.

    As variáveis categóricas foram codificadas numericamente usando OneHotEncoder para serem processadas pelo modelo.

Tipo de Problema

Este é um tipo de problema de regressão, onde o objetivo é prever um valor numérico contínuo, a nota do IMDb.

O projeto testou dois modelos de regressão:

    Regressão Linear: Um modelo mais simples e rápido, que apresentou um bom resultado.

    Random Forest Regressor: Um modelo de alto desempenho e mais complexo. Embora tenha sido testado, o desempenho inicial pode melhorar usando variáveis mais relevantes.

Medidas de Performance

As métricas de avaliação do modelo foram:

    RMSE (Root Mean Squared Error): Mede a magnitude média dos erros do modelo. Um valor mais próximo de zero indica melhor performance.

    R² (Coeficiente de Determinação): Indica a proporção da variância dos dados que é explicada pelo modelo. O valor varia de 0 a 1, quando mais próximo de 1 mais ajustado o modelo está.

4. Execução e Resultados do Modelo

Execute o arquivo previsao_nota_imdb.py para rodar o modelo e obter a previsão da nota IMdb.

Resultados:

    Modelo de Regressão Linear:

        Nota IMDB Prevista: 9.27

        RMSE: 0.201

        R²: 0.387

    Modelo Random Forest:

        Nota IMDB Prevista: 8.77

        RMSE: 0.199

        R²: 0.398

5. Modelo de treinamento salvo em .pkl