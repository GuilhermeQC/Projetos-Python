a = int(input("Informe o primeiro termo da PA: \n"))
qtd = int(input("Informe a quantidade de termos da PA: \n"))
d = int(input("Informe a razão da PA: \n"))

PA = []

for n in range(1, qtd+1):
    termos = a+(n-1)*d
    PA.append(termos)
print(f'Os termos dessa P.A. são: {PA}')
soma = sum(PA)
print(f"A soma dos termos da P.A. são: {soma}")