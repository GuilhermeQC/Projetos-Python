def resposta_bool(perg):
    resposta = input(perg).strip().lower()
    if resposta in ["sim", "s"]:
        return True
    elif resposta in ["não", "n", "nao"]:
        return False
    else:
        print("Resposta inválida. Por favor, reponda corretamente!")
        return resposta_bool(perg)


pergunta = "Deseja cadastrar um novo curso? \n"
pergunta2 = "Deseja realizar um novo cadastro? \n"
cadastro = resposta_bool(pergunta)

while cadastro == True:
    nome = str(input("Digite o nome do curso:\n"))
    codigo = int(input("Informe o código do curso (Ex: '0000')\n"))
    vagas = int(input("Informe a quantidade de vagas:\n"))
    masc = int(input("Informe a quantidade de candidatos do sexo masculino:\n"))
    fem = int(input("Informe a quantidade de candidatos do sexo feminino:\n"))

    print(f"Para o Curso de {nome}, de código {codigo}, existem:\n"
          f"{vagas} vagas disponíveis.\n"
          f"{masc+fem} candidatos cadastrados, no total de {(masc+fem)/vagas:.2f} candidatos por vaga.\n"
          f"Tendo {fem*100/(masc+fem):.2f}% dos candidatos do sexo feminino.\n")

    cadastro = resposta_bool(pergunta2)
print ("Fim!")