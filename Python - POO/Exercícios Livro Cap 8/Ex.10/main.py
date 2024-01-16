from cartesiano import Ponto

ponto1 = Ponto("Ponto_1", -2, -2)
ponto2 = Ponto("Ponto_2", -1, -1)
ponto3 = Ponto("Ponto_3", 0, 0)
ponto4 = Ponto("Ponto_4", 1, 1)
ponto5 = Ponto("Ponto_5", 2, 2)


lista_pontos = [ponto1, ponto2, ponto3, ponto4, ponto5]

cont = 0
for i in lista_pontos:
    print(lista_pontos[cont])
    cont += 1

print(
    f"A distância eucliciana entre: {ponto1.nome} e {ponto5.nome} é de: {ponto1.distancia(ponto5)}")
