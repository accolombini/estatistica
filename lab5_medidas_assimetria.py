# As medidas de assimetria nos auxiliam a compreender como os dados estao dispersos se existem algum comportamento simetrico ou nao
# Na construcao de um histograma estamos interessados em saber a forma da distribuicao dos dados =>> Coeficiente de assimetria de Pearson (As) dado por: |||> As = (μ - Μ0) / σ ou As = (X - M0) / S => sabendo que M0 e a moda dos dados
# Podemos classificar as distribuicoes de frequencia segundo sua assimetria: Simetrica (As = 0) => Assimetrica negativa (As < 0) e Assimetrica positiva (As > 0)
# Medidas de curtose =>> estao interessadas em quantificar a concentracao ou a dispersao dos valores de um conjunto de dados em relacao as medidas de tendencia central ||> elas medem o grau de achatamento de uma distribuicao sendo complementar as informacoes de dispersao =>> assim, as medidas de curtose alem de complementarem as medidas de tendencia central elas complementam as medidas de disprsao ||> K = (Q3 - Q1) / (2 * (P90 - P10))
# As medidas de curtose sao classificadas em tres categorias ||> Leptocurtica => dados MUITO concentrados em torno do centro (K < 0.263); ||> Mesocurtica => dados LEVEMENTE concentrados em torno do centro (K = 0.263); ||> Platicurtica => dados POUCO concentrados em torno do centro (K > 0.263)
# Boxplot => concentra num unico grafico varios indicadores de estatistica descritiva e nos fornece uma ideia de assimetria e dispersao ||> um boxplot concentra 5 tipos de medidas estatisticas sao elas <> Valor minimo; <> Valor maximo; <> Mediana (Q2); <> Primeiro quartil (Q1); <> Terceiro quartil (Q3). Alem disso, um boxplot nos oferece a ideia de: <> Poicao; <> Dispersao; <> Assimetria; <> Caudas valores extremos; <> Dados discrepantes (outliers)
# Como analisar um boxplot >>= <> Posicao central -> corpo: MEDIANA ou Q2; <> Dispersao -> dq = Q3 - Q2; <> Assimetria -> posicoes relativas entre Q1(P25), Q2(P50) e Q3(P75) -> corpo do boxplot; <> O tamanho da cauda sao dados por linhas sendo os extremos os pontos de maximo e minimo  calculados como segue: <> Min = Q1 - 1.5 * dq; Max = Q3 + 1,5 * dq => lembrando que dq e a medida de dispersao dada por dq = Q3 - Q2 <> o que estiver alem dos extremos de Min e Max sao os outliers <> Q3 - Q1 nos fornece 50% dos dados sob analise


import seaborn as sns
from bokeh.sampledata.iris import flowers as dados 
import matplotlib.pyplot as plt 


# Boxplot em Python
print('Vamos incialmente visualizar nossos dados')
print(dados.head())
print(dados.shape)
print(dados.describe())
print('\nVamos agora representar estes dados numa estrutura de boxplot usando seaborn => observe')
sns.boxplot(data=dados)
plt.show()
# Vamos agora realizar algumas customizacoes no nosso boxplot
sns.set(style='whitegrid', color_codes=True)
sns.boxplot(data=dados)
plt.show()

# Vamos agora usar o matplotlib para gerar nosso boxplot
plt.boxplot(dados['sepal_length'])
plt.show()
plt.boxplot(dados['sepal_width'])
plt.show()
plt.boxplot(dados['petal_length'])
plt.show()
plt.boxplot(dados['petal_width'])
plt.show()
