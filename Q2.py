strB = "55"
strA = str(input()).split(" ")

cont = 0

for c in range(0, len(strA)):
    if(strB in strA[c]):
        cont = cont + 1

print(f"O texto 55 ocorre {cont} vez(es) na entrada lida.")

