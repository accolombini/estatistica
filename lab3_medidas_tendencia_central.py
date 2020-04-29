# Nesta pratica faremos uma revisao geral sobre os fundamentos estatisticos por tras do conceitos de Medidas de Tendencia Central => MTC
# MTC >>= sao assim chamadas por indicarem um ponto em torno do qual se concentram os dados
# Como neste momento estamos falando de estatistica descritiva, queremos descrever os dados => em outra palavras estamos falando de medidas descritivas para resumir dados.
# Se as MTC forem calculadas a partir de dados populacionais nos temos PARAMETROS
# Se as MTC forem calculadas a partir de dados amostrais nos temos ESTIMADORES ou ESTATISITCAS
# Se a palavra ESTATISTICA estiver no PLURAL => ESTATISTICAS >>= estamos falando de Media; Moda; Mediana e Percentis
# Para alinharmos => em termos de notacao das estatisticas temos as seguintes descricoes:
# 1- Medidas => Numero de elementos N (Parametros) ou n (Estimadores)
# 2- Media => μ (Parametros) e X ̅ (Estimadores)
# 3- Variancia => σ² (Parametros) e S² (Estimadores)
# 4- Desvio Padrao => σ (Parametros) e S (Estimadores) 
# 1 Vamos iniciar os estudos de MTC falando inicialmente da Media Aritmetica
# Definicao => a media aritmetica X ̅ e a soma de todos os valores observados da variavel dividida pelo numero de observacoes. Geometricamente e o centro de gravidade que representa o ponto de equilibrio de um conjunto de dados
# Caracteristicas >>= sao facilmente encontradas; sao muito sensiveis as variacoes dos dados; a soma da diferenca de cada valor observado em relacao a media e zero, ou seja, a soma dos desvios e zero. =>> importante para a definicao de variancia que sera visto a seguir <=> Σ (Xi - X ̅) = 0
# Atencao => importante ||> uma desvantagem da media aritmetica e o fato dela ser fortemente afetada por valores extremos (outliers)
# 2 Nossa segunda medida de MTC e a Moda => que representa a maior frequencia da variavel entre os valores observados
# 3 Nossa terceira medida de MTC e a Mediana => e o valor que ocupa a posicao central dos dados ordenados => nao se esqueca de ordenar os dados e se acontercer de ter um conjunto par de valores, voce devera tirar a media aritmetica dos valores centrais
# 4 Nossa quarta intervencao da estatistica descritiva e juntar essas medidas e avaliar o que podemos extrari de informacao >>= as tres medidas juntas ||> Media aritmetica; Moda e Mediana nos passam uma idaia de como os dados estao => podem ter Assimetria a esquerda (Media < Mediana < Moda) => podem ser Simetricos (Media == Mediana == Moda) => podem ter Assimetria a direita (Moda < Mediana < Media)
# Vamos agora para as MTC chamadas de Medidas Separatrizes Quartis e Percentis => seu objetivo e separar o conjunto de valores em partes de igual tamanho ||> sao medidas muito importantes -> dividem o conjunto de dados em partes iguais, podendo ser: <> Quartil => divide o conjunto de dados em 4 partes iguais; <> Decil => divide o conjunto de dados em 10 partes iguais; <> Percentil => divide os dados em 100 partes iguais <$> importante a ordenacao dos dados
# 1 Quartil => divide o conjunto de dados em quatro partes iguais! <> 1º Quartil -> 25% dos dados sao menores ou iguais ao valor do primeiro quartil => p = 0,25(n + 1)
# 2 Ja o segundo quartil que e exatamente a mediana <> 2º Quartil -> 50% dos daos sao valores menores ou iguais ao valor do segundo quartil => p = 0,5(n + 1)
# 3 no terceiro quartil <> 3º Quartil -> 75% dos dados sao valores menores ou iguais ao valor do terceiro quartil => p = 0,75(n + 1)
# Medidas separatrizes => Percentis dividem o conjunto de dados em 100 partes iguais, como exemplo podemos escrever 5º Percentil => P5 -> 5% dos dados sao valores menores ou iguais ao valor do quinto percentil => p = 0,05(n + 1); <> 10º Percentil => P10 -> 10% dos dados sao valores menores ou iguais ao valor de decimo percentil => p = 0,10(n + 1)



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.sampledata.iris import flowers as dados 


# 1- Praticando MTC com Python => uma olhada rapida nos dados
print('\nObservando nossos dados')
print(dados.shape)
print(dados.head())
print(type(dados))
print(dados.describe())

# Calculando a media => ja fizemos isso, mas vale o aprendizado
print('\nCalculo da Media')
print(dados.mean())

# Calculando a media para cada variavel individualmente => por variavel queremos dizer por coluna
med_sl = np.mean(dados['sepal_length'])
print('\nA media de sepal_length e: ', med_sl)

med_sw = np.mean(dados['sepal_width'])
print('\nA media de sepal_width e: ', med_sw)

med_pl = np.mean(dados['petal_length'])
print('\nA media de petal_length e: ', med_pl)

med_pw = np.mean(dados['petal_width'])
print('\nA media de petal_width e: ', med_pw)

# Uma terceira forma de calcular as medias e usando a biblioteca numpy => observe
print('\nUsando numpy para o calculo da media das variaveis numericas')
print(np.mean(dados))

# Vamos agora calcular a MEDIANA => lembrando que para seu calculo devemos ordenar os dados e pegar o valor central
mediana_sl = np.median(dados['sepal_length'])
print('\nCalculo da mediana usando numpy: mediana_sl', mediana_sl)
mediana_sw = np.median(dados['sepal_width'])
print('\nCalculo da mediana usando numpy: mediana_sw', mediana_sw)
mediana_pl = np.median(dados['petal_length'])
print('\nCalculo da mediana usando numpy: mediana_pl', mediana_pl)
mediana_pw = np.median(dados['petal_width'])
print('\nCalculo da mediana usando numpy: mediana_pw', mediana_pw)

# Vamos agora calcular a MODA => lembrando que para seu calculo implica em encontrar o valor que se repete o maior numero de vezes >>= para este calculo nao vamos mais utilizar a biblioteca numpy => vamps trabalhar com os recursos do DataFrame =>> Observe que sera apresentado dois valores, sendo, o primeiro referente ao numero de valores que se enquadram em quanto moda e o segundo a moda propriamente dita, por exemplo, os valores 0 e 5 siginifica que há apenas uma moda e seu valor e 5. Note que no caso de petal_length temos dois valores sinalizados como moda: 0 -> 1.4 e 1 -> 1.5 => isso nos mostra que os valores 1.4 e 1.5 aparecem o mesmo numero de vezes
moda_sl = dados['sepal_length'].mode()
print('\nCalculo da moda usando numpy: moda_sl', moda_sl)
moda_sw = dados['sepal_width'].mode()
print('\nCalculo da moda usando numpy: moda_sw', moda_sw)
moda_pl = dados['petal_length'].mode()
print('\nCalculo da moda usando numpy: moda_pl', moda_pl)
moda_pw = dados['petal_width'].mode()
print('\nCalculo da moda usando numpy: moda_pw', moda_pw)

# Calculo das medidas =>> Separatrizes -> percentis e quartis => trabalhando com numpy
# Como exemplo, vamos trabalhar com o Percentil 10, o processo é o mesmo para qualquer valor de Percentile
print('\nVamos calcular o percentil 10 P10')
P10_sl = np.quantile(dados['sepal_length'], 0.10)
print('O percentil 10 dos dados sepal_length P10_sl: ', P10_sl)
P10_pl = np.quantile(dados['petal_length'], 0.10)
print('O percentil 10 dos dados spetal_length P10_pl: ', P10_pl)
P10_sw = np.quantile(dados['sepal_width'], 0.10)
print('O percentil 10 dos dados sepal_width P10_sw: ', P10_sw)
P10_pw = np.quantile(dados['petal_width'], 0.10)
print('O percentil 10 dos dados petal_width P10_pw: ', P10_pw)

# Para os quartis o processo tambem e o mesmo >>= observe que faremos uso do mesmo metodo .quantile()
print('\nVamos trabalhar com os quartis')
Q1_sl = np.quantile(dados['sepal_length'], 0.25)
print('O primeiro quartil dos dados sepal_length Q1_sl: ', Q1_sl)
Q2_sl = np.quantile(dados['sepal_length'], 0.5)
print('O segundo quartil dos dados sepal_length Q2_sl: ', Q2_sl)
Q3_sl = np.quantile(dados['sepal_length'], 0.75)
print('O terceiro quartil dos dados sepal_length Q3_sl: ', Q3_sl)

# Vamos agora plotar os graficos para estatistica descritiva
# Para iniciar nossos trabalhos, vamos visualizar novamente nossos dados
print('\nOlhando a estrutura para definirmos o que plotar')
print(dados.head())
# 1- Plotar a relacao entre sepal_length x sepal_width 
x = dados['sepal_length'] 
y = dados['sepal_width']
plt.scatter(x,y)
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.show()
# 2- Vamos agora adiconar a este grafico o ponto medio destes dados
plt.scatter(x,y)
plt.plot(np.mean(x), np.mean(y), 'vr')
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.show()
# 3- Vamos agora adicionar a mediana e a moda neste grafico
plt.scatter(x,y)
plt.plot(np.mean(x), np.mean(y), 'vr')
plt.plot(np.median(x), np.median(y), '^y')
plt.plot(x.mode(), y.mode(), '<r')
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.show()
# 4- Vamos repetir os graficos para os dados faltantes petal_length x petal_width >>= note que deixei comentado o calculo da moda => lembre-se que temos dois valores para a moda, experimente executar o codigo eleminando o comentario e observe o que acontece
x1 = dados['petal_length'] 
y1 = dados['petal_width']
plt.scatter(x1,y1)
plt.plot(np.mean(x1), np.mean(y1), 'vr')
plt.plot(np.median(x1), np.median(y1), '^y')
# plt.plot(x1.mode(), y1.mode(), '<r')
plt.xlabel('petal_length')
plt.ylabel('petal_width')
plt.show()
