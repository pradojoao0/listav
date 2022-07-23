


vetA = [int(i) for i in input().split(" ") if i]
vetB = [int(i) for i in input().split(" ") if i]

vetC = [0 for i in range(len(vetA) + len(vetB))]

ittA = 0
ittB = 0

for c in range(0, len(vetC)):
    if(c == 0 or c % 2 == 0):
        vetC[c] = vetA[ittA]
        ittA = ittA + 1
    else:
        vetC[c] = vetB[ittB]
        ittB = ittB + 1


texto = " ".join(map(str, vetC))
print(texto)
