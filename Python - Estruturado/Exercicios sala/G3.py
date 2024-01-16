import random

numeros = [3, 4, 1, 2, 2, 3, 4 ,5 ,6, 9, 10, 12, 11, 13]
print (numeros)

numeros.sort()
print (numeros)

numeros.sort(reverse=True)
print(numeros)

copia = list(numeros)
random.shuffle(copia)
if copia == numeros:
    numeros.clear
    print(f"Lista cópia: {copia}")
else: 
    print("A lista não é igual a original!")

contagem = numeros.count(2)
print(f"Contagem do elemento: {contagem}")

elementos = len(numeros)
print (f"Elementos: {elementos}")

menor = min(numeros)
print (menor)

maior = max(numeros)
print (maior)

media = sum(numeros)/len(numeros)
print (f"{media:.2f}")

for numero in numeros:
    print (numero)