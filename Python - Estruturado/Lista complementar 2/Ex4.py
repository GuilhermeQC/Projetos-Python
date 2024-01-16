# O programa em que calcule o Valor a Pagar pela conta de energia elétrica para uma determinada Classe Consumidora.
x = True
while x == True:
    print("Escolha a classe consumidora!\n"
          "1. Classe A\n"
          "2. Classe B\n"
          "3. Classe C")
    classe = int(input())

    if classe == 1:
        print("Para a classe A: Tarifa de R$0,50 por Kw/h gastos!\n")
        tarifa = 0.5
        consumo = float(input("Digite o consumo de energia em Kw/H!\n"))
        VF = consumo * tarifa
        ICMS = (0.3 * VF)
        VP = VF + ICMS
        print(f"O valor a pagar por seu consumo energético é de: R${VP:.2f}!")
        break

    if classe == 2:
        print("Para a classe A: Tarifa de R$0,80 por Kw/h gastos!\n")
        tarifa = 0.8
        consumo = float(input("Digite o consumo de energia em Kw/H!\n"))
        VF = consumo * tarifa
        ICMS = (0.3 * VF)
        VP = VF + ICMS
        print(f"O valor a pagar por seu consumo energético é de: R${VP:.2f}!")
        break

    if classe == 3:
        print("Para a classe A: Tarifa de R$1,00 por Kw/h gastos!\n")
        tarifa = 1
        consumo = float(input("Digite o consumo de energia em Kw/H!\n"))
        VF = consumo * tarifa
        ICMS = (0.3 * VF)
        VP = VF + ICMS
        print(f"O valor a pagar por seu consumo energético é de: R${VP:.2f}!")
        break
    else:
        print("Opção inválida!")
