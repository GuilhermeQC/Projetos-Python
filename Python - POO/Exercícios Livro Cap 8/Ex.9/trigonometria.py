import math as m


class Trigonometria:
    def __init__(self, angulo):
        self.angulo = angulo
        self.anguloRad = m.radians(angulo)

    def radiano(self):
        return self.anguloRad

    def seno(self):
        return (m.sin(self.anguloRad))

    def cosseno(self):
        return (m.cos(self.anguloRad))

    def tangente(self):
        return (m.tan(self.anguloRad))

    def __str__(self):
        return (f"O angulo {self.angulo}° graus em radiano é: {self.radiano():.2f}° rad\n"
                f"O seno de: {self.angulo} é: {self.seno():.2f}\n"
                f"O cosseno de: {self.angulo} é: {self.cosseno():.2f}\n"
                f"A tangente de: {self.angulo} é: {self.tangente():.2f}\n"
                )
