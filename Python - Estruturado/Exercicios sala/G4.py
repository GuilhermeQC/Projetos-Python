import random


numeros = [3, 4, 1, 2, 2, 3, 4 ,5 ,6, 9, 10, 12, 11, 13]
print (numeros)

for i, numero in enumerate(numeros):
    print(f"{numero} está armazenado no índice: {i}")

random.shuffle(numeros)

for i, numero in enumerate(numeros):
    print(f"{numero} está armazenado no índice: {i}")