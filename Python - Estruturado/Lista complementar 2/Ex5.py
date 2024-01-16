#Calculadora de salário líquido a receber com descontos!
print ("A calculadora irá calcular seu salário líquido a receber com base nos dados informados e descontos!")
print ("A taxa referênte ao INSS segue a seguinte tabela!\n"
       "|-----------------------------------------|\n"
       "|Salário bruto                 |Alíquota  |\n"
       "|-----------------------------------------|\n"
       "|Até R$800,45                  |7,65%     |\n"
       "|De R$800,46 até R$900,00      |8,65%     |\n"
       "|De R$900,01 até R$1.334,07    |9,00%     |\n"
       "|De R$1.334,08 até R$2.668,15  |11,00%    |\n"
       "|-----------------------------------------|\n")

horas_trabalhadas = int(input("Informe as horas trabalhadas!\n"))
valor_hora = float(input("Informe o valor da hora trabalhada!\n"))
salario_bruto = horas_trabalhadas*valor_hora

print (f"O valor do salário bruto é de: {salario_bruto}")
if salario_bruto <= 800.45:
    inss = salario_bruto*0.0765
elif salario_bruto >= 800.46 or salario_bruto <= 900:
    inss = salario_bruto*0.0865
elif salario_bruto >= 900.01 or salario_bruto <= 1334.07:
    inss = salario_bruto*0.09
elif salario_bruto >= 1334.08 or salario_bruto <= 2668.15:
    inss = salario_bruto*0.11
else:
    print ("Error!")
    
print (f"O valor do salário bruto descontado o INSS é de: {salario_bruto-inss:.2f}")

imposto_renda = float()

if (salario_bruto-inss) < 1257.12:
    imposto_renda = 0
    print ("Está isento de imposto de renda!")
elif (salario_bruto-inss) >= 1257.13 or salario_bruto <= 1257.13:
    imposto_renda = (0.15*(salario_bruto-inss))-188.57
elif (salario_bruto-inss) > 2512.08:
    imposto_renda = (0.275*(salario_bruto-inss))-502.58

salario_liquido = salario_bruto - inss - imposto_renda

print (f"O salário líquido a receber vai ser de: {salario_liquido:.2f}! ")