stringInput = str(input())
strArray = []
for c in range(0, len(stringInput)):
    strArray.append(stringInput[c])

stringOutput = ""

for c in range(0, len(strArray)):
    if(strArray[c].upper() != "A" and strArray[c].upper() != "E" and strArray[c].upper() != "I" and strArray[c].upper() != "O" and strArray[c].upper() != "U"):
        stringOutput = stringOutput + strArray[c]

print(stringOutput + "QYSptAF")
