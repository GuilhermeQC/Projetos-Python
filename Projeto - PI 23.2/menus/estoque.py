import json
import os


def new_json():
    if not os.path.exists('produtos.json'):
        with open('produtos.json', 'w', encoding="utf-8") as file:
            json.dump([], file)


def clear():
    os.system('cls')


def cad_att(prod):
    object_json = json.dumps(prod, indent=4, ensure_ascii=False)
    with open("produtos.json", "w", encoding="utf-8") as file:
        file.write(object_json)


def cad_op():

    with open("produtos.json") as file:
        prod = json.load(file)
        return prod


def cad_list():
    produtos = cad_op()

    if produtos != []:
        print("Lista de produtos:")
        print(10*"=-=")
        for x, produto in enumerate(produtos):
            print(f"Descrição: {produto['desc']}\n"
                  f"Código: {produto['cod']}\n"
                  f"Quantidade: {produto['qtd']}\n"
                  f"Custo: {produto['cust']}\n"
                  f"Preço: {produto['prec']}\n"
                  f"Fornecedor: {produto['forn']}")
            print(10*"=-=")
        input("Pressione 'enter' para continuar")
    else:
        print("Não há produtos cadastrados:")
        input("Pressione 'enter' para continuar")


def cad_edit():
    produtos = cad_op()
    cad_list()
    if not produtos == []:
        selec = input(
            "Informe o código de barras do produto a ser alterado: ")
        index = None
        for p in produtos:
            if p['cod'] == selec:
                index = produtos.index(p)

                produtos[index]['desc'] = input(
                    "Digite a nova descrição do produto: ")
                produtos[index]['cod'] = input(
                    "Digite o novo código do produto: ")
                produtos[index]['qtd'] = input(
                    "Digite a nova quantidade do produto: ")
                produtos[index]['cust'] = input(
                    "Digite o novo custo do produto: ")
                produtos[index]['prec'] = input(
                    "Digite o novo preço do produto: ")
                produtos[index]['forn'] = input(
                    "Digite o novo fornecedor do produto: ")
                cad_att(produtos)
                print("Dados alterados. ")

        input("Pressione 'enter' para continuar ")


def cad_cad():
    produtos = cad_op()
    print("Cadastro de produtos:\n")
    dicionario = {
        "desc": input("Descrição do produto: "),
        "cod": input("Código do produto: "),
        "qtd": input("Quantidade do produto: "),
        "cust": input("Custo do produto: "),
        "prec": input("Preço de venda: "),
        "forn": input("Fornecedor do produto: ")}
    produtos.append(dicionario)
    cad_att(produtos)
    print("Produto cadastrado com sucesso!")
    input("Pressione 'enter' para continuar")


while True:

    new_json()

    clear()
    esc = int(input("=-=-=-=-=-=-=MENU ESTOQUE=-=-=-=-=-=-=-=\n"
                    "1 - Cadastro de produtos\n"
                    "2 - Atualizar produtos\n"
                    "3 - Listar produtos\n"
                    "4 - Sair\n"
                    "=-=-=-=-=-=-=MENU ESTOQUE=-=-=-=-=-=-=-=\n"
                    "Escolha: "))

    if esc == 4:

        clear()
        break

    if esc == 1:
        clear()
        cad_cad()

    if esc == 2:
        clear()
        cad_edit()

    if esc == 3:
        clear()
        cad_list()
