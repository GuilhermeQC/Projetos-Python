#Construa um programa que tem como dados de entrada dois pontos quaisquer no plano cartesiano: P1 e P2.

print ("O programa calculará a distância entre P1 e P2.")

print ("Insira os valores de P1: \n")
x1 = float(input("Digite o valor de X_1: "))
y1 = float(input("Digite o valor de Y_1: "))

print ("Insira os valores de P2: \n")
x2 = float(input("Digite o valor de X_2: "))
y2 = float(input("Digite o valor de Y_2: "))

from math import sqrt

dist = sqrt(((x2-x1)**2)+((y2-y1)**2))

print (f"A distância entre os pontos apresentados é de: {dist:.2f}")