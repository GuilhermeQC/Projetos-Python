ingressos = 120
valor = 5

for i in range(9):

    lucro = ingressos*valor
    print(
        f"O lucro esperado pela venda de {ingressos} ingressos a R${valor}, é de R${lucro}")
    valor -= 0.5
    ingressos += 26
