Crie um ambiente virtualizado para não instalar as dependências na versão global do python:

python -m venv .venv <------execute
.venv\Scripts\Activate.ps1 <------execute

Agora instale as bibliotecas atraves do arquivo requirements.txt:

pip install -r requirements.txt <------execute

//////////////////////////////////////////////////////////////
#1. Execute o arquivo relatorios.py para obter os relatorios análise exploratória dos dados

#2.a = Com base no 4 relatorio, eu recomendaria o filme mais popular, que atraves do grafico se notou ser o filme The Dark Night, além de realmente ser um bom filme, com base nos atributos 'No_of_Votes', 'Gross', 'Meta_score', 'Genre' e 'Director'.

#2.b = Com certeza 'No_of_Votes', 'Genre', 'Director', 'Actors' e 'Meta_score':
Numero de votos representa a popularidade do filme;
Os generos estao sempre ligados aos filmes com maior faturamento (ação, aventura, drama);
Diretores de prestigio sempre relacionados a altos faturamentos em filmes;
Atores de prestigio também tem relação com filmes de alto faturamento
Filmes com notas altas muitas vezes tem alto faturamento.

#2.c = Através da leitura da coluna 'Overview', a sinopse do filme, da para inferir o genero do filme sim, na maioria dos casos. Ao utilizar uma IA do modelo NLP, para analisar a coluna 'Overview' seria bem fácil de determinar qual o genêro do filme com base na sinopse.

#3. Quais variáveis e/ou suas transformações você utilizou e por quê?
R: Usei a variáveis numéricas = 'Released_Year', 'Runtime', 'Meta_score', 'No_of_Votes', 'Gross', e as variáveis categóricas 'Certificate', 'Genre', 'Director', 'Star1', 'Star2', 'Star3', 'Star4', para chegar no valor 'IMDB_Rating'. 
Foram feitas transformações de dados em 'Runtime' e 'Gross' para remover caracteres como texto e converter para tipo numerico. Também foram feito preenchimento de valores nulos. As variáveis categóricas foram transformadas em formato numérico usando OneHotEncoder para melhorar o processamento.

Qual tipo de problema estamos resolvendo?
R: Este problema é do tipo de regrewssão, o objetivo é prever o valor da nota IMDB, que é um valor continuo e numérico.
Usei 2 exemplos, regressão linear, mais simples e veloz e tem uma boa interpretabilidade, e me chegou no valor correto da nota IMDB. Usando o random forest regressor, que é um modelo de alto desempenho e um pouco mais complexo, usando todos os valores da tabela não consegui chegar no valor correto da nota IMBD, usando menos valores e valores mais relevantes pode ser o mais recomendado.

Qual medida de performance do modelo foi escolhida e por quê?
R: As medidas de performance utilizadas foram RMSE e R². RMSE: métrica usada para medir a magnitude média de erros, sendo assim mais fáicl de prever notas. Quanto mais próximo de 0 melhor. R²: Essa metrica indica a proporcao de variancia das variaveis de saida sendo explicada pelo modelo, valor varia de 0 a 1, quando mais proximo de 1 melhor o modelo está ajustado aos dados.

#4. Rode o arquivo previsao_nota_imdb.py
Através do modelo de regressão simples foi obtido o valor IMDB 9,27 RMSE: 0.201 R²: 0.387

Já usando o modelo random forest, usando todos os valores do filme ele chegou num valor 
IMDB 8.77 RMSE: 0.199 R²: 0.398



