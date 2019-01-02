from random import uniform, randint
arq = open("iris.txt", "r")

dados = [val.split(",")[0:-1] for val in arq]
arq.seek(0)
classe = [val.rstrip('\n')[-1] for val in arq]

dados = [[float(x) for x in line] for line in dados]
classe = [int(x) for x in classe]

classe = [-1 if elem != 1 else elem for elem in classe]
peso = [uniform(-1, 1) for x in range(5)]
alfa = 0.4
treinamento = 500

print("\nPeso inicial: ", peso)

for t in range(treinamento):
    c = randint(0, 149)
    y = 0
    entrada = [dados[c][e] for e in range(4)]
    entrada.append(1)
    se = classe[c]
    for i in range(len(peso)):
        y += entrada[i] * peso[i]
    if y >= 0:
        sr = 1
    else:
        sr = -1

    if sr != se:
        peso = [peso[x] + alfa * (se - sr) * entrada[x] for x in range(len(peso))]

acerto = 0
for c in range(150):
    y = 0
    entrada = [dados[c][e] for e in range(4)]
    entrada.append(1)
    se = classe[c]
    for i in range(len(peso)):
        y += entrada[i] * peso[i]
    if y >= 0:
        sr = 1
    else:
        sr = -1

    if sr == se:
        acerto += 1

print("\nQuantidade de treinamentos: ", treinamento)
print("\nPeso final: ", peso)
print("\nTaxa de acerto: ", 100*acerto/150, "\n")
