# . Construa um programa que solicite que o usuário informe 2 números inteiros positivos. O programa deve calcular: Média geométrica dos 2 números e o cubo do segundo!
from math import sqrt

n1 = float(input("Informe o primeiro número! \n"))
n2 = float(input("Informe o segundo número! \n"))

print(f"O cubo do segundo número informado é de: {n2**3:.1f}")
print(f"A média geométrica entre o primeiro e o segundo número é de: {sqrt((n1*n2))}")
