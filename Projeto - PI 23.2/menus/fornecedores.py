import json
import random
import os


def new_json():
    if not os.path.exists('fornecedores.json'):
        with open('fornecedores.json', 'w', encoding="utf-8") as file:
            json.dump([], file)


def clear():
    os.system('cls')


def for_op():
    with open('fornecedores.json') as file:
        fornecedores = json.load(file)
        return fornecedores


def for_att(fornecedor):
    object_json = json.dumps(fornecedor, indent=4, ensure_ascii=False)
    with open("fornecedores.json", "w", encoding="utf-8") as file:
        file.write(object_json)


def cadastrar_fornecedor():

    fornecedores = for_op()

    codigo = random.randint(100000, 999999)
    nome = input("Digite o nome do fornecedor: ")
    telefone = input("Digite o telefone do fornecedor: ")
    email = input("Digite o email do fornecedor: ")

    fornecedores[codigo] = {
        'Nome': nome,
        'Telefone': telefone,
        'Email': email
    }

    print("Fornecedor cadastrado com sucesso!")
    input("Pressione 'enter' para continuar")


def visualizar_fornecedores():
    fornecedores = for_op
    if fornecedores != []:
        print("Lista de Fornecedores:")
        for codigo, fornecedor in fornecedores.items():
            print(f"Código: {codigo}")
            for chave, valor in fornecedor.items():
                print(f"{chave}: {valor}")
            print("--------------------")
            input("Pressione 'enter' para continuar")
    else:
        print("Não há fornecedores cadastrados!")
        input("Pressione 'enter' para continuar")


def buscar_fornecedor():
    fornecedores = for_op()
    codigo = input("Digite o código do fornecedor que deseja buscar: ")
    if fornecedores != []:
        if codigo in fornecedores:
            print(f"Detalhes do fornecedor (Código: {codigo}):")
            fornecedor = fornecedores[codigo]
            for chave, valor in fornecedor.items():
                print(f"{chave}: {valor}")
                input("Pressione 'enter' para continuar")
        else:
            print("Fornecedor não encontrado.")
            input("Pressione 'enter' para continuar")
    else:
        print("Não há forneceodres cadastrados!")
        input("Pressione 'enter' para continuar")


while True:
    new_json()
    clear()
    print("\nCadastro de Fornecedores")
    print("1. Cadastrar Fornecedor")
    print("2. Visualizar Fornecedores")
    print("3. Buscar Fornecedor")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        clear()
        cadastrar_fornecedor()
    elif opcao == '2':
        clear()
        visualizar_fornecedores()
    elif opcao == '3':
        clear()
        buscar_fornecedor()
    elif opcao == '4':
        clear()
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
