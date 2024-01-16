#Calculdora equacional

from math import sqrt

print ("Uma equação de 2° Grau é dada pela seguinte formula [Ax²+Bx+C = 0]\n"
       "Para calcula-lá é preciso saber identificar os valores [A,B,C] e organizar a equação."
       "Em sequência é aplicado a fórmula de bhaskara. E é nessa parte que o programa entra!")

a = float(input("Digite o valor de A\n"))
b = float(input("Digite o valor de B\n"))
c = float(input("Digite o valor de C\n"))

if a and b and c != 0:
    delta = ((b**2)-4*a*c)
    print ("A equação possui duas soluções reais!")
    x1 = ((-b)+sqrt(delta))/2
    x2 = ((-b)-sqrt(delta))/2
    print (f"As raízes dessa equação são: X'= {x1} e X'' = {x2}")
else:
    print ("A Equação não pode existir!")