class Ponto:
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y
    def __str__(self):
        return (f"Nome: {self.nome} || Coordenadas: {self.x, self.y}")
