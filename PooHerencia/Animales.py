class Animal:
    def __init__(self, nombre, alimento, edad, raza):
        self._nombre = nombre
        self._alimento = alimento
        self._edad = edad
        self._raza = raza

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def alimento(self):
        return self._alimento

    @alimento.setter
    def alimento(self, alimento):
        self._alimento = alimento

    @property
    def edad (self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def raza(self):
        return self._raza

    @raza.setter
    def raza(self, raza):
        self._raza = raza

    def alimentarse(self):
        print(f"Me alimento de: {self._alimento}")

    def __str__(self):
        return f"Animal: nombre: {self._nombre}, alimento: {self._alimento}, edad {self._edad}, raza: {self._raza}"

class Perro(Animal):
    def __init__(self, nombre, alimento, edad, raza):
        super().__init__(nombre, alimento, edad, raza)

class Gato(Animal):
    def __init__(self, nombre, alimento, edad, raza):
        super().__init__(nombre, alimento, edad, raza)

class Caballo(Animal):
    def __init__(self, nombre, alimento, edad, raza):
        super().__init__(nombre, alimento, edad, raza)

perro = Perro("Pochita", "Raza", 3, "Cuzco")
gato = Gato("Kittie", "Gatuno", 1, "Egipcio")
caballo = Caballo("Supah", "Caballuno", 5, "Gigante")
print(perro)
print(gato)
print(caballo)
perro.alimentarse()
gato.alimentarse()
caballo.alimentarse()