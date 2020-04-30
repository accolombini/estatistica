# Nesta pratica faremos uso das ferramentas estudadas para desenvolver uma analise em cima de precos de acoes 


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


# Lendo o arquivo csv
df = pd.read_csv('D:\\Users\Angelo\AULAS\\PETR4.SA.csv')
print('\nExplorando os dados')
print(type(df))
print(df.head())
print(df.tail())
print(df.shape)
print('\nUsando describe() para uma visao descritiva dos nossos dados')
print(df.describe())
print('\nCapturando informacoes gerais do nosso DataFrame')
print(df.info())

# 1- Vamos agora calcular o coeficiente de variacao CV = δ / x * 100
CV = df.std() / df.mean() * 100
print('\nO coeficiente de variacao da PETR4')
print(CV)

# 2- Agora vamos trabalhar com histogramas
nome = 'Volume'
df[nome].hist()
plt.xlabel('Preco', size=14)
plt.ylabel('Frequencia', size=14)

# 3- Calculando a mediana e media => usaremos o mesmo grafico para 2 e 3
plt.plot(df[nome].median(), 0, '*r')
plt.plot(df[nome].mean(), 0, 'og')
plt.show()

# 4- Trabalhando com boxplot -> numpy e seaborn
df.iloc[:, 0:6].boxplot()
plt.show()
sns.boxplot(data=df.iloc[:, 0:6])
plt.show()

# 5- Grafico de linhas
df.iloc[:, 0:6].plot()
plt.show()
