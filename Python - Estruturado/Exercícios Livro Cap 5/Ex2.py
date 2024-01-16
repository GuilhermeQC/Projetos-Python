qtd = int(input("Informe a quantidade de nadadores: \n"))
nadadores = []
tempos = []

for cont in range(qtd):

    print(f"Informe o nome do {cont+1}° nadador: ")
    nadadores.append(input())
    print(f"Informe o tempo do {cont+1}° nadador: ")
    tempos.append(float(input()))

menor = min(tempos)
indice = tempos.index(min(tempos))

print(
    f"O nadador {nadadores[indice]} obteve o menor tempo de: {menor} segundos!")
