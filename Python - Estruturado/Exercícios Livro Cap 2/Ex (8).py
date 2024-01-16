#Construa um programa que receba do usuário o valor do salário mínimo atual. Na sequência, o programa deve solicitar que o usuário informe o valor do seu salário mensal. Ao fim, o 
#programa deve calcular a quantidade de salários mínimos recebidos pelo usuário.

salario_minimo = float(input("Informe o salário mínimo atual. \n"))
salario_usuario = float(input("Informe o seu salário. \n"))

salario_recebido = (salario_usuario*100)/salario_minimo

print (f"O seu salário recebido é igual a: {salario_recebido/100}x o salário mínimo!")
