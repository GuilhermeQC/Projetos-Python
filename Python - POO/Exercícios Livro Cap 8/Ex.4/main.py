from lista import Lista

elementos = int(input("Quantidade de elementos da lista: "))
lista_teste = []
for i in range(elementos):

    elemento = input("Informe uma palavra: ")
    lista_teste.append(elemento)

lista_teste1 = Lista(lista_teste)
lista_teste1.exibirLista()
