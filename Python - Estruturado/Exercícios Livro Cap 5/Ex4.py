
from math import factorial

N = int(input("Digite um número ímpar, maior que 1: "))
if N <= 1 or N % 2 == 0:
    print("O número não atende os requisitos. ")
else:
    lista = []
    for x in range(N):
        numero = int(input("Digite um número maior ou igual a zero: "))
        lista.append(numero)

    central = int(len(lista)/2)
    elemento_central = lista[central]
    fatorial = factorial(elemento_central)
    print(f"A lista é: {lista}")
    print(f"Portanto, {elemento_central}! = {fatorial}")

#Simulando a função fatorial:
    # fatorial = 1  # 1 é o valor que nunca alterará o produto
    # for n in range(2, elemento_central + 1):
        # fatorial *= n  # fatorial = fatorial * n