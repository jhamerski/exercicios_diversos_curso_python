import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier

# Lendo o arquivo
arquivo = pd.read_csv('D:\\Faculdade Jonas\\5Fase\\Inteligencia_Artificial\\vinho\\wine_dataset.csv')

# print(arquivo.head())

# Substituindo os valores por 0 e 1
arquivo['style'] = arquivo['style'].replace('red', 0)
arquivo['style'] = arquivo['style'].replace('white', 1)

# Verificando o tamanho do arquivo
print(f'O arquivo tem tamanho: {arquivo.shape}\n')

# Separando variáveis
y = arquivo['style']
x = arquivo.drop('style', axis=1)

# Criando conjunto de dados de treino e teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.1)
print(f'Treino com {x_treino.shape} e teste com {x_teste.shape}\n')

# Criação do modelo
modelo = ExtraTreesClassifier()
modelo.fit(x_treino, y_treino)

# Imprimindo % de resultados
resultado = modelo.score(x_teste, y_teste)
print(f'Precissão de: {resultado}\n')

# Gabarito
print(f'Gabarito de y_teste:\n{y_teste[400:403]}\n')
print(f'Restante dos dados x_teste:\n{x_teste[400:403]}')

# Previsões
previsoes = modelo.predict(x_teste[400:403])
print(f'Previsão: {previsoes}')
