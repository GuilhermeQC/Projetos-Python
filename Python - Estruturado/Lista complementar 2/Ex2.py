# Programa gerador de receita. O remédio possui 500mg por ml (ml contém 20 gotas)

nome = str(input("Digite o nome do paciente! \n"))
idade = int(input("Informe a idade do paciente! \n"))
peso = float(input("Informe o peso do paciente! (Modelo: 99.9) \n"))
if idade >= 12:
    if peso >= 60:
        print("Para pacientes com 12 anos ou mais e com 60kg ou mais deve se tomar:")
        print("************************************************************************ \n"
              f"O paciente {nome} deve tomar 40 gotas do remédio, equivalente a 1000mg! \n"
              "************************************************************************")
    else:
        print("Para pacientes com 12 anos ou mais e com peso menor que 60kg deve se tomar:")
        print("************************************************************************ \n"
              f"O paciente {nome} deve tomar 35 gotas do remédio, equivalente a 875mg! \n"
              "************************************************************************")
else:
    print("Para pacientes com menos de 12 anos a dosagem é referente ao peso!")
    if peso >= 5 or peso <= 9:
        
        print("************************************************************************ \n"
              f"O paciente {nome} deve tomar 5 gotas do remédio, equivalente a 125mg! \n"
              "************************************************************************")
    elif peso >= 9.001 or peso <= 16:
       
        print("************************************************************************ \n"
              f"O paciente {nome} deve tomar 10 gotas do remédio, equivalente a 250mg! \n"
              "************************************************************************")
    elif peso >= 16.001 or peso <= 24:
        
        print("************************************************************************ \n"
              f"O paciente {nome} deve tomar 15 gotas do remédio, equivalente a 375mg! \n"
              "************************************************************************")
    elif peso >= 24.001 or peso <= 30:

        print("************************************************************************ \n"
              f"O paciente {nome} deve tomar 20 gotas do remédio, equivalente a 500mg! \n"
              "************************************************************************")
    elif peso > 30:
        print("")
    else:
        print("O medicamento não possui recomendação para essa faixa de peso e idade. Não é recomendado o uso do medicamento!")