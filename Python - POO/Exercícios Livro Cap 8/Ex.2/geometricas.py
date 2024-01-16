from math import pi

class Retangulo:
    def __init__(self, lar, alt):
        self.lar = lar
        self.alt = alt
        
    def calcularPerimetro(self):
        return (self.lar+self.alt)*2
    
    def calcularArea(self):
        return (self.alt * self.lar)

class Circulo:
    
    def __init__(self, raio):
        self.raio = raio
    def calcularArea(self):
        return (pi*(self.raio)**2)
    def calcularVolume(self):
        return (4/3*pi*(self.raio)**2)
