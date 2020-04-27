# Nesta pratica faremos uma revisao geral sobre os modelos de graficos mais utilizados em estatistica descritiva utilizando Python
# 1 Vamos iniciar com graficos de Barras e Colunas


import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np


# Gerando dados para graficos de barras (variaveis longas) e grafico de colunas (variaveis curtas)
x = ['N1', 'N2', 'N3', 'N4', 'N5', 'N6']
x2 = ['Variavel Um', 'Variavel Dois', 'Variavel Tres', 'Variavel Quatro', 'Variavel Cinco', 'Variavel Seis',]
y = [2, 5, 2, 7, 5,1]

# Grafico de barras
plt.figure(figsize=(13,6))
plt.barh(x2, y, color='y')
plt.title('Grafico de Barras', size=20)
plt.xlabel('Variavel x', size=20)
plt.ylabel('Categorias', size=18)
plt.show()
# Grafico de colunas
plt.figure(figsize=(6,6))
plt.bar(x, y, color='c')
plt.title('Grafico de Colunas', size=20)
plt.xlabel('Variavel x', size=20)
plt.ylabel('Categorias', size=18)
plt.show()
# Vamos agora usar a biblioteca seaborn
sns.barplot(x,y)
plt.title('Grafico de Colunas', size=20)
plt.xlabel('Variavel x', size=20)
plt.ylabel('Categorias', size=18)
plt.show()

# 2 Agora vamos trabalhar com graficos de setores => dividem um circulo em setores proporcionais as frequencias observadas nas categorias (indicado para variaveis categoricas -> pequeno numero => maximo 6) >>= indicados para comparar valor da categoria especifica com o total numero de categorias pequenas
# Gerando grafico de setores
plt.figure(figsize=(8,8))
plt.pie(y, labels=x, radius=1.2)
plt.title('Grafico de Setores', size=12)
plt.show()

# 3 Agora vamos trabalhar com graficos de linhas => sao os principais recursos para a representacao de series temporais >>= tambem conhecidos por graficos de series cronologicas => normalmente no eixo x temos algo relativo ao tempo e no eixo y algo relacionado a uma grandeza que esteja variando no tempo
# Gerando graficos de linhas
y = [6, 8, 3, 1, 9]
x1 = [1, 2, 3, 4, 5]
x = ['seg', 'ter', 'qua', 'qui', 'sex']
plt.figure(figsize=(8,8))
plt.plot(x1, y, 'v-', color='r')
plt.title('Grafico de linhas', size=20)
plt.xlabel('Variavel X', size=20)
plt.ylabel('Variavel Y', size=20)
plt.show()
# Outro grafico => observe a customizacao
plt.figure(figsize=(8,8))
plt.plot(x, y, 'o-.c')
plt.title('Grafico de linhas', size=20)
plt.xlabel('Variavel X', size=20)
plt.ylabel('Variavel Y', size=20)
plt.show()

# 4 Histogramas => formados por colunas justapostas para representar distribuicao de frequencia em dados >>= no eixo horizontal temos os limites das classes de agrupamento =>> no heixo Y sempre estaremos representando a frequencia e no eixo X temos os limites das classes de agrupamento (chamadas de bins no Python)
# Gerando Histogramas
# Vamos gerar dados usando randn -> gera numeros aleatorios respeitando uma distribuicao normal de meida zero e desvio padrao igual a 1
x = np.random.randn(1000)
# Gerando o histograma => acompanhe
plt.figure(figsize=(7,7))
plt.hist(x, bins=10, color='c')
plt.title('Histograma', size=20)
plt.xlabel('Eixo X', size=20)
plt.ylabel('Eixo Y', size=20)
plt.show()
