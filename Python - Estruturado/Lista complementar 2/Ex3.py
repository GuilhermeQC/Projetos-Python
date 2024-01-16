# NOTAS PARA SALTO ORNAMENTAL; 6 NOTAS, A MAIOR E A MENOR DEVEM SER EXCLUIDAS DA MÉDIA!

print("**Calculadora de nota**")

nota = float()
soma = float()

x = 0
while x < 6:
    x += 1

    nota = float(input("Digite a nota do juruado! \n"))

    if x == 1:
        maior = nota
        menor = nota
    if nota > maior:
        maior = nota
        soma += nota
    elif nota < menor:
        menor = nota
        soma += nota
    else:
        soma += nota

print(f"A soma das notas dos juízes desconsiderando a maior e menor nota foi de: {soma - maior - menor}")