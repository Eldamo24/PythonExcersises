class Cafetera:
    def __init__(self, capMax, capAct):
        self._capMax = capMax
        self._capAct = capAct

    def __str__(self):
        return f"Cafetera: Capacidad actual: {self._capAct}, Capacidad maxima: {self._capMax}"

    @property
    def capMax(self):
        return self._capMax

    @capMax.setter
    def capMax(self, capMax):
        self._capMax = capMax

    @property
    def capAct(self):
        return self._capAct

    @capAct.setter
    def capAct(self, capAct):
        self._capAct = capAct

    def llenarCafetera(self):
        self._capAct = self._capMax

    def vaciarCafetera(self):
        self._capAct = 0

    def ingresarCafe(self, cantidad):
        self._capAct += cantidad
        if self._capAct > self._capMax:
            self._capAct = self._capMax

    def servirTaza(self, cantCafe):
        if cantCafe <= self._capAct:
            self._capAct -= cantCafe
            print("La taza de lleno")
        else:
            self._capAct = 0
            print("La taza no se lleno")

def crearCafetera():
    capMax = int(input("Ingrese capacidad maxima de la cafetera: "))
    return Cafetera(capMax, capMax)

cafetera = crearCafetera()
cafetera.vaciarCafetera()
print(cafetera)
cafetera.llenarCafetera()
print(cafetera)
cafetera.vaciarCafetera()
cafetera.ingresarCafe(25)
print(cafetera)
cafetera.servirTaza(10)
print(cafetera)