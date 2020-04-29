# Monte Carlo => tecnica que faz uso de numeros aleatorios para obter areas abaixo de curvas =>> obter integrais. Nesta pratica queremos encontra oo valor de π a partir de numeros aleatorios (pense no circulo de raio R cincunscrito em um quadrado) => nosso objetivo sera gerar numeros aleatorios dentro desse quadrado (vamos considerar apenas um quarto do circulo e tambem que o raio sera igual a 1) =>> note que ao gerar esses numeros aleatorios uma parte devera cair dentro do meu setor (circunferencia) a a outra parte devera cair fora. So lembrando a area da circunferencia e dada por π r² => neste caso nosso valor de π  sera dado por π = (4 * Setor) / r². Em termos numericos podemos escrever π = (Ι * 4) / Τ => onde I = numeros gerados aleatoriamente internos ao setor e T o total de numeros aleatorios gerados


import random


# Calculo de π usando Monte Carlo
T = 80000
print('Total de sorteios: ', T)
print('\nI sera nossa variavel que ira conter os pontos gerados internamente ao setor => queremos encontrar (equacao da circunferencia) x² + y² = R, onde R = 1')
I = 0
for i in range(T):
    x = random.random()
    y = random.random()
    if (((x * x) + (y * y)) < 1):
        I += 1
print('\nNossos valores => I = ', I)
print('O valor de => T = ', T)
PI = 4 * I / T
print('\nNosso valor de π: ', PI)
# Para praticar altere os valores T e confira o valor encontrado para π
