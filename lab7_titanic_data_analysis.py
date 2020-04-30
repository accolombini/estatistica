# Nesta pratica vamos explorar os dados do Titanic aplicando as tecnicas de estatistica descritivas estudadas ate aqui


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


# Lendo os dados do arquivo .csv
df = pd.read_csv('D:\\Users\Angelo\AULAS\\titanic_train.csv')
print('\nExplorando os dados')
print(type(df))
print(df.head())
print(df.tail())
print(df.shape)
print('\nNote que describe() elimina as informacoes categoricas')
print(df.describe())
print('\nCapturando informacoes gerais do nosso DataFrame')
print(df.info())
# Da primeira analise foi possivel observar que existem dados faltantes, vamoa agora trabalhar isso com Python e coletar informacoes mais precisas a esse respeito =>> acompanhe
print('\nAvaliar quantos dados faltantes existem no nosso DataFrame')
print(df.isnull().sum())
# Uma das tecnica para preencher os dados faltantes e atraves da media ou com a mediana =>> você devera testar outras formas e avaliara que melhor atende seus requisitos de analise
print('\nPreenchendo dados faltantes com a mediana')
df.fillna(df['Age'].dropna().median(), inplace=True)
print('\nAvaliando se ainda existem dados faltantes')
print(df.isnull().sum())

# Vamos agora plotar alguns graficos
# 1- Queremos saber o numero de sobreviventes em relacao a tarifa paga Fare
df.plot(kind='scatter', x = 'Fare', y = 'Survived', color='r', linewidth = 1)
plt.show()
# 2 Grafico de barras relacionando a classe com os sobreviventes
sns.barplot(x = 'Pclass', y = 'Survived', data=df)
plt.show()
# 3 Grafico boxplot sobreviventes em relacao ao sexo
sns.barplot(x = 'Sex', y = 'Survived', data=df)
plt.show()
# 4 Graficos com Informações de Idade e Sexo

survived = 'survived'
not_survived = 'not survived'

fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(10, 4))
women = df[df['Sex']=='female']
men = df[df['Sex']=='male']

ax = sns.distplot(women[women['Survived']==1].Age.dropna(), bins=18, label = survived, ax = axes[0], kde =False)
ax = sns.distplot(women[women['Survived']==0].Age.dropna(), bins=40, label = not_survived, ax = axes[0], kde =False)
ax.legend()

ax.set_title('Female')
ax = sns.distplot(men[men['Survived']==1].Age.dropna(), bins=18, label = survived, ax = axes[1], kde = False)
ax = sns.distplot(men[men['Survived']==0].Age.dropna(), bins=40, label = not_survived, ax = axes[1], kde = False)
ax.legend()
_ = ax.set_title('Male')
plt.show()
