# Neste laboratorio vamos avaliar como as Medidas de Dispersao MD contribuem no processo de analise juntamente com as Medidas de Tendencia Central MTC
# Medidas de dispersao => sabemos que os dados apresentam semelhancas e variabilidades
# As MD =>> permitem avaliar ate que ponto os resultados se concentram ou nao ao redor da tendencia central de um conjunto de observacoes
# Sabemos que os dados apresentam semelhancas e variabilidades, podendo apresentar <$> Assimetria a Esquerda; ||> Assimetria a Direita; ||> Serem perfeitamente Simetricos (Media, Mediana e Moda => coincidentes) <$> Embora, possamos identificar as tendencias atraves das MTCs podemos resolver esse assunto utilizando as MD
# Medidas de dispersao (MD) |||> as MD auxiliam as MTC a melhor descrever os dados =>> nos indicam o quanto os dados estao ou nao proximos uns dos outros </> Nao faz sentido algum calcular a media de um conjunto de dados onde nao ha variacao do seus elementos <$> Precisamos de uma MTC e MD para descrever adequadamente os dados =>> Importante!!!
# As medidas de dispersao MD mais importantes sao: Amplitude total; => Amplitude interquartilica; => Desvio medio; => Variancia e desvio-padrao; => Coeficiente de variacao
# Amplitude Total ||> esta relacionada a diferenca entre o maior e o menor valor observado; Nao leva em consideracao valores intermediarios; Nao temos informacoes de como os dados estao distribuidos =>> { 7,5,5,5,4,4, 99, 7, 8, 9, 1, 1} => A = 99 - 1 = 98
# Amplitude Interquartilica ||> por definicao e dada pela diferenca entre o primeiro e o terceiro quartil; => e uma medida mais estavel do que a amplitude total; => abrange 50% dos dados; => e muito util para se detectar valores discrepantes (outliers) |||> dq = Q3 - Q1 =>> A amplitude semi-interquartilica dqm = (Q3 - Q1)/2 
# Desvio Medio MD |||> como o proprio nome nos diz ele nos fornece a diferenca entre cada valor observado e a media, sendo dado por: (xi - μ) -> (Xi - X). Sabemos que a soma dos desvios e igual a ZERO (entao como podemos calcular o MD?) => sera preciso trabalhar com modulos, em outra palavras precisamos desconsiderar os sinais utilizando o modulo e a media dessas diferencas, a isso, damos o nome de desvio medio |||> dm = (Σ|xi - μ|) / n ou dm = (Σ|Xi - X|) / N
# Variancia e Desvio Padrao <$> a necessidade da variancia e do disvio padrao surgiu porque possuimos algumas desvantagens em relacao ao desvio medio (por exemplo, no ponto zero a funcao modular nao possui derivada) =>> para amenizar esses problemas utilizamos o desvio padrao e a variancia, sendo =>> σ^2 = (Σ(xi - μ)^2) / n; =>> S^2 = (Σ(Xi - X)^2) / (n - 1) ||> observe que a variancia/desvio padrao eliminam o problema do desvio medio substituindo os valores modulares por valores quadraticos (a funcao quadratica e diferenciavel no ponto x = 0) |||> O desvio padrao retorna a dimensao original dos dados (elimina o quadrado), assim o desvio padrao e a raiz quadrada da variancia, sendo expresso por σ ou S (sempre eum numero positivo)
# Coeficientes de Variacao =>> muito importante quando queremos comparar algo proveniente de fenomenos distintos e precisamos normalizar |||> indica a variabilidade da medida em relacao a media => CV = (x / σ) * 100 <$> a vantagem de sua utilizacao e que ela nos permite comparar a dispersao de diferentes distribuicoes com diferentes medias e desvios padroes. Vamos tentar entender um pouco mais isso =>> qual das distribuicoes tem maior dispersao dos dados (heterogeneidade da populacao)? 1- SALINIDADE: 32 +/- 6,4 2- PH: 8,2 +/- 1,64 (em palavras SALIDADE tem media igual a 32 e desvio de +/- 6,4 e PH tem media 8,2 e desvio de +/- 1,64). O que queremos saber, qual das distribuicoes apresenta maior dispersao dos dados (heterogeneidade da populacao? ||> 6,4 / 32 & 100 = 20% ε 1,64 / 8,2 * 100 = 20% <=> ou seja, temos o mesmo coeficiente de variacao para ambos os conjuntos de dados


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from bokeh.sampledata.iris import flowers as dados


# 1- Amplitude total em Python
print('\nRelembrando nossos dados')
print(dados.head())
print(dados.shape)
print(type(dados))
print(dados.describe())

# Calculo da Amplitude maxima >>= observe a presenca de uma variavel categorica e o contorno que faremos para resolver o problema
print('\nPara o calulo da Amplitude maxima precisamos encontrar os valores maximos e minimos')
print('\nVamores maximos')
print(dados.max())
print('\nVamores minimos')
print(dados.min())
print('\nCapturando os dados numericos do DataFrame -> uso do metodo .iloc()')
print(dados.iloc[:, 0:4])
print('\nExtraindo valores maximos')
print(dados.iloc[:, 0:4].max())
print('\nExtraindo valores minimos')
print(dados.iloc[:, 0:4].min())
print('\nCalculo da amplitude maxima - Valores maximo - Valores minimos')
print(dados.iloc[:, 0:4].max() - dados.iloc[:, 0:4].min())

# Outra forma de obter os mesmos resultados
print('\nOutra forma de obter os mesmos resultados - usando numpy')
print('\nExtraindo valores maximos')
print(np.max(dados.iloc[:, 0:4]))
print('\nExtraindo valores minimos')
print(np.min(dados.iloc[:, 0:4]))
print('\nCalculo da amplitude maxima - Valores maximo - Valores minimos')
print(np.max(dados.iloc[:, 0:4]) - np.min(dados.iloc[:, 0:4]))

# 2- Calculo da Amplitude Interquartilica dq = Q3 - Q1 em Python
print('\nPodemos calcular usando DataFrame ou atraves da biblioteca numpy')
print('Usando pandas - exemplo')
print(np.quantile(dados['sepal_length'], 0.75))
print('\nTrabalhando com DataFrame')
print(dados['sepal_length'].quantile(0.75))
print('\nCalculo da Amplitude Interquartilica')
print(dados['sepal_length'].quantile(0.75) - dados['sepal_length'].quantile(0.25))
# Podemos usando DataFrame realizar todos os calculos de uma so vez
print('\nCalculando tudo de uma vez')
print(dados.quantile(0.25))
print(dados.quantile(0.75))
print('\nA amplite maxima e')
print(dados.quantile(0.75) - dados.quantile(0.25))
# Podemos usando pandas realizar todos os calculos de uma so vez
print('\nCalculando tudo de uma vez com numpy')
print('\nA amplite maxima e')
print(np.quantile(dados.iloc[:, 0:4], 0.75) - np.quantile(dados.iloc[:, 0:4], 0.25))

# 3- Desvio medio Absoluto
print('\nCalculo do desvio medio Absoluto')
print(dados.mad())

# 4- Calculo da Variancia e Desvio Padrao - usando DataFrame
print('\nCalculo do Variancia por DataFrame')
print(dados.var())
print('\nCalculo do Desvio Padrao por DataFrame')
print(dados.std())
# Calculo da Variancia e Desvio Padrao - usando a biblioteca Numpy
print('\nCalculo do Variancia usando Numpy')
print(np.var(dados))
print('\nCalculo do Desvio Padrao usando Numpy')
print(np.std(dados))

# 5- Coeficiente de variacao usando Python => CV = σ/x * 100 ou ...
print('\nO coeficiente de variacao por definicao e: CV = S/X * 100')
print('\nPrimeiro vamos usar Numpy')
print(np.std(dados)/np.mean(dados) * 100)
print('\nPor ultimo vamos usar DataFrame')
print(dados.std()/dados.mean() * 100)
