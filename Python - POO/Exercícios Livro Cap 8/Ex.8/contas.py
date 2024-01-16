from clientes import Cliente
import random


def gerarNumero():
    lista = []
    for i in range(5):
        num = random.randint(0, 9)
        lista.append(str(num))
    numConta = int(''.join(lista))
    return numConta


class ContaInvestimento:
    def __init__(self, cliente, saldo, taxaJuros):
        self.cliente = cliente
        self.conta = gerarNumero()
        self.saldo = saldo
        self.taxaJuros = taxaJuros

    def aumentarJuros(self):  # Aplica juros na conta
        self.saldo += ((self.taxaJuros/100)*self.saldo)
        return self.saldo

    # def exibirExtrato(self):
    #     print(f"Cliente: {self.cliente.nome}||", end="")
    #     print(f" Conta: {self.conta}")
    #     print(f"Saldo: {self.saldo}||", end="")
    #     print(f" Taxa de juros: {self.taxaJuros}%")
    def exibirExtrato(self):
        return self.cliente.nome, self.conta, self.saldo, self.taxaJuros