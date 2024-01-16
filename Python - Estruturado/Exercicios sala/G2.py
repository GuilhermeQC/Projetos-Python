import random


atrizes = ["Adriana Prado","Bárbara Borges", "Camila Queiroz", "Danielle Winits"]
print (f"Lista : {atrizes}")

random.shuffle(atrizes)
print (f"Lista embaralhada: {atrizes}")

atrizes.sort()
print (f"Lista ordem crescente: {atrizes}")
atrizes.sort(reverse=True)
print (f"Lista decrescente: {atrizes}")
