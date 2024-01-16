class Cliente:
    def __init__(self, nome, telefone, cpf):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf

    def getDados(self):
        return self.nome, self.cpf, self.cpf

