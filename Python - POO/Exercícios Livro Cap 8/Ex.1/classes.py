class Ingressos:
    def __init__(self, evento, valor):
        self.evento = evento
        self.valor = valor
    def exibirValor(self):
        return self.valor
    def __str__(self):
        return ("O nome do evento é {}, e o valor do ingresso é: {:.2f}").format(self.evento, self.valor)
    