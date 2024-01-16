from classes import Ingressos
import os

os.system('cls')

evento1 = Ingressos("Rock in Rio - 2024", 654.99)

print(evento1.__str__())
print(evento1.exibirValor())
