class Calculadora:
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def somar(self):
        return (self.op1 + self.op2)

    def subtrair(self):
        return (self.op1 - self.op2)

    def multiplicar(self):
        return (self.op1 * self.op2)

    def dividir(self):
        return (self.op1 / self.op2)

    def potencia(self):
        return (self.op1 ** self.op2)
