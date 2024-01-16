from random import shuffle
from random import choice
nomes = []

print("Digite o nome dos compradores da Rifa, para sortear digite 0")
while True:
    nome = (input("Informe o nome de quem comprou a rifa.\n"))

    if nome != "0":
        nomes.append(nome)
    elif nome == "0":
        print(f"Cadastro encerrado."
              f"Os compradores são: {nomes}")
        shuffle(nomes)
        sorteado = choice(nomes)
        print(f"O nome sorteado foi: {sorteado}")
        break
