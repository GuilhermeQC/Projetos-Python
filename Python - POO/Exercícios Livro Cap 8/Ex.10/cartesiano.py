from math import sqrt
class Ponto:
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y
    def __str__(self):
        return (f"Nome: {self.nome} || Coordenadas: {self.x, self.y}")

    def distancia(self, q):
        d = sqrt((self.x-q.x)**2 + (self.y - q.y)**2)
        return d
    
