from math import sqrt

def segundograu(a,b,c):
    delta = b**2-4*a*c
    print (delta)
    if delta > 0:
        raiz = sqrt(delta)
        x1 = (-(b)+raiz)/(2*a)
        x2 = (-(b)-raiz)/(2*a)
        resultado = []
        resultado.append(x1)
        resultado.append(x2)
        return resultado

    if delta == 0:
        raiz = sqrt(delta)
        x = (-(b)+raiz)/(2*a)
        return x

    if delta < 0:
        print("A raiz dessa equação não existe no conjunto dos números Reais")

print ("Calculadora de equação de segundo grau.")
n1 = float(input("Insira o valor de A \n"))
n2 = float(input("Insira o valor de B \n"))
n3 = float(input("Insira o valor de C \n"))
print("As raizes da equação são de:")
print(segundograu(n1,n2,n3))

