from Bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        Bicicleta.__init__(self, color, ruedas, tipo)
        self._velocidad = velocidad
        self._cilindrada = cilindrada

    @property
    def velocidad(self):
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
        Bicicleta.toString(self)
        print(f"Velocidad: {self._velocidad} \nCilindrada: {self._cilindrada}")