# Programa calculo valor estacionamento

HE = int(input("Digite a hora de entrada! \n"))
ME = int(input("Digite o minuto de entrada! \n"))
HS = int(input("Digite a hora de saída! \n"))
MS = int(input("Digite o minuto de saída! \n"))

TaxaMinutos = 4/60
HR = HS - HE
MR = MS - ME

if HR < 0:
    HR = HR*(-1)
if MR < 0:
    MR = MR*(-1)

HoraMinutos = HR*60
MinutosTotais = MR+HoraMinutos

Valor = MinutosTotais * TaxaMinutos

print (f"O valor a ser pago no estacionamento será de: R${Valor:.3}")