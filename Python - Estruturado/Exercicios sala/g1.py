compras = []
confirm = True
print ("Menu lista de compras:\n"
        "1. Para adicionar um item à lista de compras\n"
        "2. Para remover um item da lista de compras\n"
        "3. Para listar a lista de compras\n"
)
selec = int(input())
while confirm == True:

    if selec == 1:
        compras.append(input("Digite o nome do produto:\n"))
        print ("Produto adicionado com sucesso!")
        

    elif selec == 2:
        compras.remove(input("Digite o nome do produto."))

    elif selec == 3:
        print (f"Os itens da lista são: {compras}")
        print ("Programa finalizado!")
        confirm = False