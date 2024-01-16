from calculadora import Calculadora

opsoma = Calculadora(1, 2)
print(f"A soma dos dois números é: {opsoma.somar()}")
opsub = Calculadora(2, 1)
print(f"A subtração dos dois números é: {opsub.subtrair()}")
opmulti = Calculadora(5, 5)
print(f"A multiplicação dos dois números é: {opmulti.multiplicar()}")
opdiv = Calculadora(100, 2)
print(f"A divisão dos dois números é: {opdiv.dividir()}")
oppot = Calculadora(5, 2)
print(f"A potência do primeiro número pelo segundo é de: {oppot.potencia()}")