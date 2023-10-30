#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=#
# Autor : Guilherme Queiroz de Carvalho
# IFBA - 2023.2: Lab. de Programação - LPR002
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=#

# Importa as bibliotecas a serem utilizadas:
import json
import os


# Caso os arquivos .JSON ainda não existam, serão criados:
if not os.path.exists('users.json'):
    with open('users.json', 'w') as file:
        json.dump([], file)
if not os.path.exists('livros.json'):
    with open('livros.json', 'w') as file:
        json.dump([], file)



# Função para limpar o terminal:
def limpar():  
    os.system('cls')



# Função que importa as informações de um dicionário ("Usuários") python para o arquivo .JSON:
def atualizar_usuarios(users):
    object_json = json.dumps(users, indent=4, ensure_ascii=False)

    with open("users.json", "w") as file:
        file.write(object_json)



# Função que importa as informações de um dicionário ("Livros") python para o arquivo .JSON:
def atualizar_livros(livros):
    object_json = json.dumps(livros, indent=4, ensure_ascii=False)

    with open("livros.json", "w") as file:
        file.write(object_json)



# Função que exporta as informações de arquivo .JSON para um dicionário ("Usuários") python:
def ler_usuarios():
    with open("users.json") as file:
        usuarios = json.load(file)
        return usuarios



# Função que exporta as informações de arquivo .JSON para um dicionário ("Livros") python:
def ler_livros():
    with open("livros.json") as file:
        livros = json.load(file)
        return livros



# Função que obtem o ID do último usuário cadastrado:
def user_id(usuarios):  
    if usuarios:
        return usuarios[-1].get('ID', 0)
    return 0



# Função que obtem o ID do último livro cadastrado:
def livro_id(livros):  
    if livros:
        return livros[-1].get('ID', 0)
    return 0


# Função que procura ID do usuário existe, procura e verifica se o livro escolhido pode ser emprestado ou não:
def emprestar_livro(id_usuario, id_livro):
    usuarios = ler_usuarios()
    livros = ler_livros()

    usuario_encontrado = False
    for usuario in usuarios:
        if usuario.get('ID') == id_usuario:
            usuario_encontrado = True
            for livro in livros:
                if livro.get('ID') == id_livro:
                    if not livro.get('Emprestado'):
                        livro['Emprestado'] = True
                        livro['ID_Usuario'] = id_usuario
                        atualizar_livros(livros)
                        print("Livro emprestado com sucesso.")
                    else:
                        print("Livro já emprestado.")
                    break  # Sair do loop dos livros
            break  # Sair do loop dos usuários

    if not usuario_encontrado:
        print("Usuário não encontrado.")


#Função que procura através da ID as informações atreladas ao empréstimo dele e remove os dados caso esteja emprestado:
def devolver_livro(id_livro):
    livros = ler_livros()

    for livro in livros:
        if livro.get('ID') == id_livro:
            if livro.get('Emprestado'):
                livro['Emprestado'] = False
                livro.pop('ID_Usuario', None)
                atualizar_livros(livros)
                print("Livro devolvido com sucesso.")
                return
            else:
                print("Livro não está emprestado.")
                return

    print("Livro não encontrado.")



# Comandos de inicialização
limpar()
print("Bem vindo!")



while True:  # Loop infinito para o funcionamento do programa em ciclo, encerando somente se solicitado:
    limpar()
    esc = int(input("Sistema gerenciador de biblioteca pessoal: \n"
                    "1 - Cadastrar comodatários: \n"
                    "2 - Atualizar comodatários:\n"
                    "3 - Listar comodatários: \n"
                    "4 - Cadastrar livros: \n"
                    "5 - Atualizar livros:\n"
                    "6 - Listar livros: \n"
                    "7 - Emprestar livros: \n"
                    "8 - Devolver livros: \n"
                    "9 - Encerrar programa: \n"
                    "Escolha uma opção: \n"))

    if esc == 9:  # Finaliza o programa:
        limpar()
        print("Fim!")
        break

    elif esc == 1:  # Cadastra um comodatário:

        limpar()
        usuarios = ler_usuarios()
        id = user_id(usuarios) + 1

        print("Informe os dados para o cadastro: ")
        nome = input("Informe o nome completo: ")
        cpf = input("Informe o CPF do comodatário: ")
        tel = input("Informe o número de telefone: ")
        end = input("Informe o endereço: ")

        dicionario = {
            "ID": id,
            "Nome completo": nome,
            "CPF": cpf,
            "Telefone": tel,
            "Endereço": end
        }

        usuarios.append(dicionario)
        atualizar_usuarios(usuarios)
        print("Comodatário cadastrado com sucesso!")
        cont = input("\nPressione 'Enter' para continuar: ")
        

    elif esc == 2:  # Atualiza dados dos comodatário a partir do ID de cadastro:

        limpar()
        usuarios = ler_usuarios()

        if not usuarios == []:  # Se o arquivo .Json não estiver em branco:

            print("Lista de comodatários: ")
            print(10*"=-=")
            for x, usuario in enumerate(usuarios):

                print(f"ID: {usuario['ID']}\n"
                      f"Nome: {usuario['Nome completo']}\n"
                      f"CPF: {usuario['CPF']}\n"
                      f"Telefone: {usuario['Telefone']}\n"
                      f"Endereço: {usuario['Endereço']}")
                print(10*"=-=")

            user_selec = int(
                input("Selecione o ID do comodatário a ser alterado: "))
            for d in usuarios:
                if d.get('ID') == user_selec:
                    usuarios[user_selec-1]['Nome completo'] = str(
                        input("Novo nome: "))
                    usuarios[user_selec-1]['CPF'] = input("Novo CPF: ")
                    usuarios[user_selec -
                             1]['Telefone'] = input("Novo telefone: ")
                    usuarios[user_selec -
                             1]['Endereço'] = input("Novo endereço: ")
                    atualizar_usuarios(usuarios)
                    cont = input("\nPressione 'Enter' para continuar: ")
        else:  # Se o arquivo .Json estiver em branco:
            print("Ainda não há comodatários cadastrados para alterar dados.")
            cont = input("\nPressione 'Enter' para continuar: ")

    elif esc == 3:  # Listar comodatários cadastrados:

        limpar()
        usuarios = ler_usuarios()

        if not usuarios == []:  # Se o arquivo .Json não estiver em branco:

            print("Lista de comodatários: ")
            print(10*"=-=")
            for x, usuario in enumerate(usuarios):

                print(f"ID: {usuario['ID']}\n"
                      f"Nome: {usuario['Nome completo']}\n"
                      f"CPF: {usuario['CPF']}\n"
                      f"Telefone: {usuario['Telefone']}\n"
                      f"Endereço: {usuario['Endereço']}")
                print(10*"=-=")
            cont = input("\nPressione 'Enter' para continuar: ")

        else:  # Se o arquivo .Json estiver em branco:
            print("Ainda não há comodatários cadastrados.")
            cont = input("\nPressione 'Enter' para continuar: ")

    elif esc == 4:  # Cadastra um livro:

        limpar()
        livros = ler_livros()
        id = livro_id(livros)+1

        print("Informe os dados para o cadastro: ")
        titulo = input("Informe o título do livro: ")
        autor = input("Informe o autor do livro: ")
        editora = input("Informe a editora do livro: ")
        ano = input("Informe o ano de publicação do livro: ")

        dicionario = {
            "ID": id,
            "Título": titulo,
            "Autor": autor,
            "Editora": editora,
            "Ano pub.": ano
        }

        livros.append(dicionario)
        atualizar_livros(livros)

        print("Livro cadastrado com sucesso!")
        cont = input("\nPressione 'Enter' para continuar: ")

    elif esc == 5:  # Atualiza dados dos livros a partir do ID de cadastro
        limpar()
        livros = ler_livros()

        if not livros == []:  # Se o arquivo .Json não estiver em branco:

            print("Lista de comodatários: ")
            print(10*"=-=")
            for x, livro in enumerate(livros):

                print(f"ID: {livro['ID']}\n"
                      f"Nome: {livro['Título']}\n"
                      f"CPF: {livro['Autor']}\n"
                      f"Telefone: {livro['Editora']}\n"
                      f"Endereço: {livro['Ano pub.']}")
                print(10*"=-=")

            user_selec = int(
                input("Selecione o ID do comodatário a ser alterado: "))
            for d in livros:
                if d.get('ID') == user_selec:
                    livros[user_selec-1]['Título'] = str(
                        input("Novo título: "))
                    livros[user_selec-1]['Autor'] = input("Novo autor: ")
                    livros[user_selec-1]['Editora'] = input("Nova editora: ")
                    livros[user_selec -
                           1]['Ano pub.'] = input("Novo ano de publicação: ")
                    atualizar_livros(livros)
                    cont = input("\nPressione 'Enter' para continuar: ")

        else:  # Se o arquivo .Json estiver em branco:
            print("Ainda não há livros cadastrados para alterar dados.")
            cont = input("\nPressione 'Enter' para continuar: ")

    elif esc == 6:  # Listar livros cadastrados:
        limpar()
        livros = ler_livros()

        if not livros == []:  # Se o arquivo .Json não estiver em branco:

            print("Lista de livros: ")
            print(10*"=-=")
            for x, livro in enumerate(livros):

                print(f"Título: {livro['Título']}\n"
                      f"Autor: {livro['Autor']}\n"
                      f"Editora: {livro['Editora']}\n"
                      f"Ano de Publicação: {livro['Ano pub.']}")
                

                print(10*"=-=")
            cont = input("\nPressione 'Enter' para continuar: ")

        else:  # Se o arquivo .Json não estiver em branco:
            print("Ainda não há livros cadastrados.")
            cont = input("\nPressione 'Enter' para continuar: ")

    elif esc == 7: #Empresta algum livro cadastrado
        limpar()
        usuarios = ler_usuarios()
        livros = ler_livros()
        if not usuarios == []:
            print("Lista de comodatários: ")
            print(10*"=-=")
            for usuario in usuarios:
                print(f"ID: {usuario['ID']}\n"
                    f"Nome: {usuario['Nome completo']}\n"
                    f"CPF: {usuario['CPF']}\n"
                    f"Telefone: {usuario['Telefone']}\n"
                    f"Endereço: {usuario['Endereço']}")
                print(10*"=-=")

            id_usuario = int(input("Selecione o ID do comodatário: "))
            limpar()
            if not livros == []:
                print("Lista de livros disponíveis: ")
                print(10*"=-=")
                for livro in livros:
                    if not livro.get('Emprestado'):
                        print(f"ID: {livro['ID']}\n"
                            f"Título: {livro['Título']}\n"
                            f"Autor: {livro['Autor']}")
                        print(10*"=-=")

                id_livro = int(input("Selecione o ID do livro a ser emprestado: "))

                emprestar_livro(id_usuario, id_livro)
                
                cont = input("\nPressione 'Enter' para continuar: ")
            else:
                print("Não há livros cadastrados, não é possivel emprestar livros:")
                cont = input("\nPressione 'Enter' para continuar: ")

        else:
            print("Não há comodatarários cadastrados no sistema:")
            cont = input("\nPressione 'Enter' para continuar: ")

    elif esc == 8: #Devolve algum livro emprestado
        limpar()
        livros = ler_livros()
        if not livros == []:
            print("Lista de livros emprestados: ")
            print(10*"=-=")
            for livro in livros:
                if livro.get('Emprestado'):
                    print(f"ID: {livro['ID']}\n"
                        f"Título: {livro['Título']}\n"
                        f"Autor: {livro['Autor']}")
                    print(10*"=-=")

            id_livro_devolver = int(input("Selecione o ID do livro a ser devolvido: "))
            devolver_livro(id_livro_devolver)
            cont = input("\nPressione 'Enter' para continuar: ")
        else:
            print("Não há livros cadastrados no sistema:")
            cont = input("\nPressione 'Enter' para continuar: ")

    else:  # Em caso de erro, o programa executará um aviso de erro:
        print("Opção inválida.")
        cont = input("Aperte 'Enter' para continuar: ")