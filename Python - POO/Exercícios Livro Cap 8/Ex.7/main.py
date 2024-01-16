from carro import Carro

carro1 = Carro(12.4)

print(carro1.andar())
print(f"A quantidade de combustível no carro1 é de: {carro1.exibirCombustivel()}")
carro1.abastecer()
print(f"A quantidade de combustível no carro1 é de: {carro1.exibirCombustivel()}")
print(f"Quilometros andado com o carro1: {carro1.andar()}")
print(f"A quantidade de combustível no carro é de: {carro1.exibirCombustivel()}")
