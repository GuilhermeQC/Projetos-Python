class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def aumentoSalario(self, porcentagem):
        self.salario += ((porcentagem/100)*self.salario)
        return self.salario
    def exibirFuncionario(self):
        return self.nome, self.salario