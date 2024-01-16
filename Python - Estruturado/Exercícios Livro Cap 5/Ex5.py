L = []

for i in range(10):
    num = int(input("Informe um número: "))
    L.append(num)

menor = min(L)
maior = max(L)
# O elemento é 2 nesse caso pq são tomados 2 números para tirar a média geométrica (Se fosse a lista inteira, o n° seria 10)
elementos = 2
# A média geométrica é calculada multiplicando todos os elementos da lista um pelo outro e tirando a raiz N deles.
mg = (menor*maior)**(1/elementos)
print(f"A média geométrica entre o maior e o menor elemento da lista é: {mg:.2f}")
