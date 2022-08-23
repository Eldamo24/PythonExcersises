from Coche import Coche

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self._carga = carga

    @property
    def carga(self):
        return self._carga

    @carga.setter
    def carga(self, carga):
        self._carga = carga

    def toString(self):
        Coche.toString(self)
        print(f"Carga: {self._carga}")