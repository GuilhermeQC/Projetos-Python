from random import randint

id_professor = randint(11000,11999)
matricula_aluno = randint(12000, 12999)

class Professor:
    def __init__(self, nome, formacao, dedicacao):
        self.nome = nome
        self.formacao = formacao
        self.dedicacao = dedicacao
        self.id = id_professor
    def getDados(self):
        return self.nome, self.formacao, self.dedicacao, self.id

class Disciplina:
    def __init__(self, nome, professor,horas):
        self.nome = nome
        self.professor = professor
        self.horas = horas
    def getDados(self):
        return self.nome, self.professor.nome, self.horas

class Aluno:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        self.nota = nota
        self.matricula = matricula_aluno
    def getDados(self):
        return self.nome, self.disciplina.nome, self.nota