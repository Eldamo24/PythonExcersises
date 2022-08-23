from Vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self._velocidad = velocidad
        self._cilindrada = cilindrada

    @property
    def velocidad (self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    @property
    def cilindrada(self):
        return self._cilindrada

    @cilindrada.setter
    def cilindrada(self, cilindrada):
        self._cilindrada = cilindrada

    def toString(self):
        Vehiculo.toString(self)
        print(f"Cilindrada: {self._cilindrada} \nVelocidad: {self._velocidad}")