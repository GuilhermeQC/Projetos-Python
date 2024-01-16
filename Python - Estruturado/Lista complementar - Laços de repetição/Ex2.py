periodo_1 = int(input("Informe o ano de inicio do período\n"))
periodo_2 = int(input("Informe o ano de término do período\n"))
nascimentos = int(input("Informe a quantidade de crianças nascidas no período\n"))
mortes = 0
masc = 0
fem = 0
tempo = 0
print ("Checagem de cada criança que nasceu:\n")
for cont in range (nascimentos):

    morta = input(f"A criança {cont+1} morreu? (S/N)\n")

    if morta == "S":
        mortes += 1
        sexo = input("Informe o sexo da criança (M/F):\n")

        if sexo == "M":
            tempo_v = int(input("Informe o tempo de vida dessa criança (Em meses)\n"))
            if tempo_v <= 24:
                tempo += 1
            masc +=1

        if sexo == "F":
            tempo_v = int(input("Informe o tempo de vida dessa criança (Em meses)\n"))
            if tempo_v <= 24:
                tempo += 1
            fem +=1

    if morta == "N":
        print ("Fora de contagem!")
              

print ("Terminar:\n"
       f"O percentual de mortalidade infantil nesse período foi de: {(mortes*100)/nascimentos}%\n"
       f"O percentual de crianças do sexo masculino que morreram foi de:{(masc*100)/nascimentos}%\n"
       f"O percentual de crianças que viveram 24 meses ou menos é de: {(tempo*100)/nascimentos}%\n")