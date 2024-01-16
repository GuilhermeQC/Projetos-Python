#Calculo de preço com taxa do Detran com base no ano

print ("Para calcular a taxa a ser paga deve ser indicado o valor do carro e o ano de fabricação!")

ano = int(input("Digite o ano de fabricação! (Modelo:XXXX)\n"))
preco = float(input("Digite o valor do carro! (Modelo: 99999.99)\n"))

if ano >= 1990:
    print("O ano de fabricação é superior à 1990, logo sua taxa será de 1,5% do valor do automóvel")
    print(f"O valor da taxa será de: R${(preco*0.015):.2f}")
elif ano < 1990:
    print("O ano de fabricação é anterior à 1990, logo sua taxa será de 1% do valor do automóvel!")
    print(f"O valor da taxa será de: R${(preco*0.01):.2f}")
else:
    print ("Alguma coisa deu erro!")
