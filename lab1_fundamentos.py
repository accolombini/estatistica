# Nesta pratica fixaremos em alguns conceitos chaves para desenvolver nossos laboratorios
# Medidas e imprecisoes do mundo <$> Estatistica => O que? =>> Estatistica e probabilidades => Como? =>> Ciencia; artigos; livros => Porque? =>> A natureza e complexa e incerta <=> dai s forte demanda pela Estatistica
# Aleatoriedade =>> trata-se de um fenomeno chave para a estatistica, pois muitos objetos de estudos da estatistica esbarram no conceito da aleatoriedade, imprecisoes em medidas e incertezas, neste contexto caotico a Estatistica nos auxilia a colocarmos luz sobre os dados e extrair informacoes. Em outras palavras a Aleatoriedade e a razao de existir da estatistica. Estatistica ||> mede -> Calculo ||> quantifica
# Fenomenos aleatorios => Mundo VUCA ->> enxergar o mundo sobre esses quatro paradigmas (Volatile, Unncertain, Complex, Ambiguous). A intuicao humana nao lida muito bem com riscos e consequentemente com incertezas
# Fenomenos aleatorios => continuacao -> nossa intuicao nao lida adequadamente com as estatisticas ||> em ciencia nada pode ser definitivamente provado, em tudo existe incertezas, em tudo existem riscos. Segundo Edgar Morin "Tudo que e ciencia pertence ao ramo da certeza (por isso pouca atencao e dada a incerteza"
# Populacao e amostra >>= apos a obtencao dos dados precisamos fazer duas perguntas: 1 -> Qual e a minha populacao? 2 -> Qual e a minha amostra?
# Populacao =>> sao todos os elementos - individuos, itens ou objetos -> cujas as caracteristicas estejam sendo estudadas
# Censo =>> e um conjunto de carcteristicas obtidas de todos os memnros da populacao
# Amostra =>> e a parte coletada a partir da populacao
# Como garantir que uma amostra represente o mais fiel possivel a populacao? |||> e preciso garantir a maxima aleatoriedade na coleta da amostra =>> em outras palavras, quanto melhor for meu processo de coleta aleatoria, melhor sera a representatividade da populacao
# Por fim e preciso saber qual o tamanho minimo de minha amostra para que ela seja representativa da minha populacao =>> responder essa questao e algo bastante complexo, ha muita teoria por tras desse fenomeno, mas e considerado num contexto geral um bom numero o valor de amostras igual a 30 (atencao isso esta longe de ser verdade absoluta e so um ponto de partida quando nada se tem)
# Medidas observadas e variaveis: Dados |> Informacoes |> Conhecimento <=> Dado != de Informacao. Dados =>> valores coletados atraves de observacao ou medicao (dados fora de contexto nao nos dizem nada!). Informacao =>> dados que sao transformados em fatos relevantes e usados para um proposito especifico
# Producao de dados ||> Dados primarios (Confiabilidade, qualidade e controle => demandam alto custo; demanda de tempo e equipe grande) =>> Coletados por quem faz a analise; sao mais confiaveis; possuem maior controle. ||> Dados secundarios (Baixo custo, rapido, apresenta diversidade => Falta controle, dados inadequados e fontes nao confiaveis) =>> Coletados por terceiros; sao nao confiaveis; nao possuem muito controle.
# Medidas observadas e variaveis |> Observacao => e uma ocorrencia de um item de dados especifico que e gravada sobre uma unidade de dados. |> Variavel => e a caracteristica de interesse que e medida em cada elemento da amostra ou populacao. Seus valores variam de elemento para elemento. As variaveis podem ter valores numericos ou nao numericos (categoricos).
# Obtendo amostras com Python
# Geracao de dados aleatorios

import random
import numpy as np 


# Gerando numeros aleatorios entre 0 -> 1
x = random.random()
print(type(x))
print('\nValores aleatorios gerados')
print(x)
# Gerando 100 numeros aleatorios
x1 = []
for i in range(100):
    x1.append(random.random())
print(type(x1))
print('\nValores aleatorios gerados')
print(len(x1))
print(x1)

# Vamos supor que temos uma populacao dada pela lista nomes a seguir
nomes = ['Lucas', 'Marcos', 'Thiago', 'Roberto', 'Bianca', 'Erika']
print('\nVamos observar nossa lista nomes')
print(nomes)

# Vamos supor que quiramos extrair uma amostra desta populacao => .choice() permite escolher aleatoriamente um componente da minha populacao/amostra
print('\nFazendo uma escolha aleatoria dentro da minha populacao')
print(random.choice(nomes))

# Imagina que agora estejamos interessados em embaralhar esta populacao (nomes) => usamos o metodo .shuffle()
print('\nEmbaralhando nossos dados -> uso do .shuffle()')
random.shuffle(nomes)
print(nomes)

# Vamos imaginar agora que nomes seja minha populacao e eu queira extrair uma amostra desta populacao de tambo igual a 3 valores => observe a flexibilidade do metodo .sample()
amostra = random.sample(nomes, 3)
print('\nImprimindo nossa amostra de 3 elementos')
print(amostra)

# Agora queremos ser capazes de reproduzir esses dados => para isso e necessario introduzir o conceito de semente =>>  usamos o metodo .seed()

random.seed(555)
x2 = []
for i in range(100):
    x2.append(random.random())
print(type(x2))
print('\nValores aleatorios gerados')
print(len(x2))
print(x2)
