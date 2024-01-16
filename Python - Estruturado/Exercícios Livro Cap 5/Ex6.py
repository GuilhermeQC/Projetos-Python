import random
L = []
produto = 1

N = int(input("Digite um valor maior que 1: "))
# Input valor>1

if N <= 1:  # Caso valor seja <= 1:
    print("O número não atende aos requisitos")
else:  # Caso o valor seja > 1:

    for i in range(N):
        aleatorio = random.randrange(100)  # Gera um valor aleatório de 0 à 100
        L.append(aleatorio)  # Coloca o valor aleatório dentro da Lista "L"

    for x in range(N):
        produto *= L[x] # Calcula o produto de todos os números pertencentes a "L"

    MG = (produto)**(1/N) # Calcula a média geométrica de todos os números da lista
    print(f"Lista: {L}\n"
          f"A média geométrica é desta lista é: {MG:.2f}")
