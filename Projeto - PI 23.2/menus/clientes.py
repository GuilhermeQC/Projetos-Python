import json
import os

def new_json():
    if not os.path.exists('clientes.json'):
        with open('clientes.json', 'w', encoding="utf-8") as file:
            json.dump([], file)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def cad_att(clients):
    with open("clientes.json", "w", encoding="utf-8") as file:
        json.dump(clients, file, indent=4, ensure_ascii=False)

def cad_op():
    with open("clientes.json") as file:
        clients = json.load(file)
    return clients

def cad_list():
    clients = cad_op()

    if clients != []:
        print("Lista de clientes:")
        print(10*"=-=")
        for x, client in enumerate(clients):
            print(f"Nome: {client['nome']}\n"
                  f"Email: {client['email']}\n"
                  f"CPF: {client['cpf']}\n"
                  f"Telefone: {client['telefone']}\n"
                  f"Endereço: {client['endereco']}")
            print(10*"=-=")
        input("Pressione 'enter' para continuar")
    else:
        print("Não há clientes cadastrados.")
        input("Pressione 'enter' para continuar")

def cad_edit():
    clients = cad_op()
    cad_list()
    if not clients == []:
        selec = input("Informe o CPF do cliente a ser alterado: ")
        index = None
        for c in clients:
            if c['cpf'] == selec:
                index = clients.index(c)

                clients[index]['nome'] = input("Digite o novo nome do cliente: ")
                clients[index]['email'] = input("Digite o novo email do cliente: ")
                clients[index]['cpf'] = input("Digite o novo CPF do cliente: ")
                clients[index]['telefone'] = input("Digite o novo telefone do cliente: ")
                clients[index]['endereco'] = input("Digite o novo endereço do cliente: ")
                cad_att(clients)
                print("Dados alterados.")

        input("Pressione 'enter' para continuar")

def cad_cad():
    clients = cad_op()
    print("Cadastro de clientes:\n")
    new_client = {
        "nome": input("Nome do cliente: "),
        "email": input("Email do cliente: "),
        "cpf": input("CPF do cliente: "),
        "telefone": input("Telefone do cliente: "),
        "endereco": input("Endereço do cliente: ")
    }
    clients.append(new_client)
    cad_att(clients)
    print("Cliente cadastrado com sucesso!")
    input("Pressione 'enter' para continuar")

while True:
    new_json()

    clear()
    print("=-=-=-=-=-=-=MENU CLIENTES=-=-=-=-=-=-=-=")
    print("1 - Cadastro de clientes")
    print("2 - Atualizar clientes")
    print("3 - Listar clientes")
    print("4 - Sair")
    print("=-=-=-=-=-=-=MENU CLIENTES=-=-=-=-=-=-=-=")

    esc = input("Escolha: ")

    if esc == '4':
        clear()
        break

    if esc == '1':
        clear()
        cad_cad()

    if esc == '2':
        clear()
        cad_edit()

    if esc == '3':
        clear()
        cad_list()
