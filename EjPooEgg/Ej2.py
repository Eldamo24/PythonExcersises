from math import pi as PI

class Circunferencia:
    def __init__(self, radio):
        self._radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, radio):
        self._radio = radio

    def area(self):
        return PI * self._radio * self._radio

    def perimetro(self):
        return 2 * PI * self._radio

def crearCircunferencia():
    radio = float(input("Ingrese radio de la circunferencia: "))
    return Circunferencia(radio)

circun = crearCircunferencia()
print(f"Area de circunferencia: {circun.area()} \nPerimetro de la circunferencia: {circun.perimetro()}")