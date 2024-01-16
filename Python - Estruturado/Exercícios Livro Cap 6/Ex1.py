relatorio = {}
while True:

    razao = input("Digite o nome do cliente: ")
    compras = int(input("Digite o valor comprado pelo cliente: "))
    relatorio.update({razao: compras})




    continuar = input("Deseja continuar? [S/N]: ")
    if continuar != "S":
        break