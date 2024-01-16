# Calculo volume de uma esfera!
import math
PI = (math.pi)

print("Para se calcular o volume de uma esfera é necessário ter dois valores,  sendo eles, o valor de Pi e o raio da esfera a ser calculada!")
print(f" O valor de Pi foi descoberto há muito tempo, ele é de: {PI:.3} aproximadamente.")

R = float(input("Insira o raio da espefera a ser calculada: \n"))

print (f"Utilizando a fórmula [Pi*R²], o volume dessa esfera será de: {4/3*PI*R**3:.2f} cm³")