class Carro:

    def __init__(self, consumo):
        #Consumo será atribuido por Km/l
        self.consumo = consumo
        self.combustivel = 0

    def exibirCombustivel(self):
        return self.combustivel
    
    def abastecer(self):
        gasosa = int(input("Quantidade, em litros, a ser abastecido: "))
        self.combustivel += gasosa
    def andar(self):
        if self.combustivel > 0:
            self.combustivel -= 1
            kmAndado = 0
            kmAndado += self.consumo
            return kmAndado
        else:
            return "Combustível está menor que 1l, abasteça para andar!"
