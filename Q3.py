vetA = [float(i) for i in input().split(" ") if i]
vetB = [float(i) for i in input().split(" ") if i]

somaValores = 0


for c in range(0, len(vetA)):
    somaValores = somaValores + (vetA[c]*vetB[c])
print(somaValores)
