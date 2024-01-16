class Disciplina:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcularMedia(self):
        return (self.notas[0] + self.notas[1]) / len(self.notas)
        
    def exibirSituacao(self):
        media = self.calcularMedia()
        if media < 6:
            return "Reprovado"
        return "Aprovado"