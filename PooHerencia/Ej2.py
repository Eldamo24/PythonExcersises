from abc import ABC, abstractmethod

class FormasGeo(ABC): #Clase abstracta

    PI = 3.1416

    @abstractmethod
    def calcularArea(self):
        pass

    @abstractmethod
    def calcularPerimetro(self):
        pass

class Rectangulo(FormasGeo):

    def __init__(self, base, altura):
        self._base = base
        self._altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        self._base = base

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        self._altura = altura

    def calcularArea(self):
        return self._base * self._altura

    def calcularPerimetro(self):
        return (self._base + self._altura) * 2

    def __str__(self):
        return f"Rectangulo: base: {self._base}, altura: {self._altura}"

class Circulo(FormasGeo):
    def __init__(self, radio):
        self._radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, radio):
        self._radio = radio

    def __str__(self):
        return f"Circulo: radio: {self._radio}"

    def calcularArea(self):
        return FormasGeo.PI * self._radio * self._radio

    def calcularPerimetro(self):
        return FormasGeo.PI * (self._radio*2)


rect = Rectangulo(10, 5)
circ = Circulo(5)
print(rect)
print(circ)
print(f"Perimetro rectangulo: {rect.calcularPerimetro()}, area: {rect.calcularArea()}")
print(f"Perimetro circulo: {circ.calcularPerimetro()}, area: {circ.calcularArea()}")

