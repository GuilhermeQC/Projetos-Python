import random
atrizes = ["Adriana Prado","Bárbara Borges", "Camila Queiroz", "Danielle Winits"]
print (f"Lista embaralhada: {atrizes}")
random.shuffle(atrizes) #Embaralha a lista
print (f"Lista embaralhada: {atrizes}")
sorteada = random.choice(atrizes)
print (sorteada)