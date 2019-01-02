from random import uniform, randint
from math import exp
arq = open("iris.txt", "r")

dados = [val.split(",")[0:-1] for val in arq]
arq.seek(0)
classe = [val.rstrip('\n')[-1] for val in arq]

dados = [[float(x) for x in line] for line in dados]
classe = [int(x) for x in classe]

v = [[uniform(-1, 1) for x in range(5)] for y in range(4)]
w = [[uniform(-1, 1) for x in range(3)] for y in range(5)]

print("\nPeso inicial da camada de entrada: ", v)
print("\nPeso inicial da camada oculta: ", w)
alfa = 0.4
treinamento = 5000
acerto = 0

for t in range(treinamento):
    c = randint(0, 149)
    z = []
    x = [dados[c][e] for e in range(4)]
    x.append(1)
    se = [-1 for x in range(3)]
    se[classe[c] - 1] = 1

    for j in range(len(v)):
        aux = 0
        for i in range(len(x)-1):
            aux += x[i] * v[i][j]
        z.append(aux)

    for j in range(len(z)):
        z[j] = 1 / (1 + exp(-z[j]))
    z.append(1)
    
    y = []
    for k in range(len(w[0])):
        aux = 0
        for j in range(len(z)):
            aux += z[j] * w[j][k]
        y.append(aux)

    for k in range(len(y)):
        y[k] = 1 / (1 + exp(-y[k]))
    
    sr = [1 if y[k] > 0.5 else -1 for k in range(len(y))]

    if sr != se:
        dy = [(se[k] - sr[k]) * y[k] * (1 - y[k]) for k in range(len(y))]

        dz = []
        for j in range(len(w)):
            aux = 0
            for k in range(len(dy)):
                aux += dy[k] * w[j][k]
            dz.append(aux)

        dz = [dz[j] * z[j] * (1 - z[j]) for j in range(len(dz))]

        v = [[v[i][j] + alfa * x[i] * dz[j] for j in range(len(v[0]))] for i in range(len(v))]
        w = [[w[j][k] + alfa * z[j] * dy[k] for k in range(len(w[0]))] for j in range(len(w))]


for t in range(150):
    z = []
    x = [dados[t][e] for e in range(4)]
    x.append(1)
    se = [-1 for x in range(3)]
    se[classe[t] - 1] = 1

    for j in range(len(v)):
        aux = 0
        for i in range(len(x)-1):
            aux += x[i] * v[i][j]
        z.append(aux)
    z.append(1)

    for j in range(len(z)):
        z[j] = 1 / (1 + exp(-z[j]))
    
    y = []

    for k in range(len(w[0])):
        aux = 0
        for j in range(len(z)):
            aux += z[j] * w[j][k]
        y.append(aux)

    for k in range(len(y)):
        y[k] = 1 / (1 + exp(-y[k]))
    
    sr = [1 if y[k] >= 0.5 else -1 for k in range(len(y))]

    if sr == se:
        acerto += 1

print("\n\nQuantidade de treinamentos: ", treinamento)
print("\nPeso final da camada de entrada: ", v)
print("\nPeso final da camada oculta: ", w)
print("\nTaxa de acerto: ", 100*acerto/150, "\n")
