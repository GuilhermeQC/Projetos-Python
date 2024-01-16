from geometricas import Retangulo
from geometricas import Circulo

Retangulo1 = Retangulo(6, 5)
print(f"O perímetro do retângulo_1 é de: {Retangulo1.calcularPerimetro():.2f} cm")
print(f"A área do retângulo_1 é de: {Retangulo1.calcularArea():.2f} cm²")

Circulo1 = Circulo(6.5)
print(f"A área desse círculo é de: {Circulo1.calcularArea():.2f} cm²")
print(f"O volume desse círculo (esfrea) é de: {Circulo1.calcularVolume():.2f} cm³")
