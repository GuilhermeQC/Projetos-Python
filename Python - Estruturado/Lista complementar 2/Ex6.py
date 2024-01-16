# Informe de calorias!

print("O programa irá calcular a soma de calorias referente à tabela de pratos ofertados!")
print("---= Pratos =---\n"
      "1. Vegetariano\n"
      "2. Peixe\n"
      "3. Frango\n"
      "4. Carne\n")

calorias  = int()

while True:
    escolha = int(input("Escolha o prato referente ao número!\n"))
    if escolha == 1:
        calorias += 180
        break
    elif escolha == 2:
        calorias += 230
        break
    elif escolha == 3:
        calorias += 250
        break
    elif escolha == 4:
        calorias += 350
        break
    else:
        print("Prato inválido!")

print("---= Sobremesas =---\n"
      "1. Abacaxi\n"
      "2. Sorvete diet\n"
      "3. Mousse diet\n"
      "4. Mousse chocolate\n")
while True:
    escolha = int(input("Escolha a sobremesa referente ao número!\n"))
    if escolha == 1:
        calorias += 75
        break
    elif escolha == 2:
        calorias += 110
        break
    elif escolha == 3:
        calorias += 170
        break
    elif escolha == 4:
        calorias += 200
        break
    else:
        print("Sobremesa inválida!")
print("---= Bebidas =---\n"
      "1. Chá\n"
      "2. Suco de laranja\n"
      "3. Suco de melão\n"
      "4. Refrigerante diet\n")
while True:
    escolha = int(input("Escolha a bebida referente ao número!\n"))
    if escolha == 1:
        calorias += 20
        break
    elif escolha == 2:
        calorias += 70
        break
    elif escolha == 3:
        calorias += 100
        break
    elif escolha == 4:
        calorias += 65
        break
    else:
        print("Bebida inválida inválida!")

print (f"A soma de calorias referente as escolhas feitas foram de: {calorias} cal")