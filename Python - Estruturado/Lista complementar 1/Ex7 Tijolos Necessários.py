# Calculo área preenchida por tijolo

CT = float(input("Digite o comprimento do tijolo: \n"))
LT = float(input("Digite a largura do tijolo: \n"))

CP = float(input("Digite o comprimento da parede: \n"))
LP = float(input("Digite a largura da parede: \n"))

areaTJ = CT*LT
areaPR = CP*LP
tijolos = areaPR/areaTJ

print(f"A área da parede é de {areaPR}cm².")
print(f"A área a ser preenchida por um tijolo é de: {areaTJ}cm²")
print(f"Serão necessários {tijolos} tijolos pare preencher a parede!")
