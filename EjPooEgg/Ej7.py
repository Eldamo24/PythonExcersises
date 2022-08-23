class Persona:
    def __init__(self, nombre, edad, sexo, peso, altura):
        self._nombre = nombre
        self._edad = edad
        self._sexo = sexo
        self._peso = peso
        self._altura = altura

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        self._sexo = sexo

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, peso):
        self._peso = peso

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        self._altura = altura

    def esMayor(self):
        if self._edad >= 18:
            return True
        else:
            return False

    def calcularIMC(self):
        imc = self._peso / (self._altura * self._altura)
        if imc < 20:
            return -1
        elif imc <= 25:
            return 0
        else:
            return 1


    def __str__(self):
        return f"Persona: Nombre: {self._nombre}, edad: {self._edad}, sexo: {self._sexo}, peso: {self._peso}, altura: {self._altura}"

def crearPersona():
    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad: "))
    sexo = input("Ingrese sexo (H, M, O): ")
    while sexo != "H" and sexo != "M" and sexo != "O":
        sexo = input("Ingrese sexo (H, M, O): ")
    peso = float(input("Ingrese peso: "))
    altura = float(input("Ingrese altura: "))
    return Persona(nombre, edad, sexo, peso, altura)

persona = crearPersona()
print(persona)
if persona.calcularIMC() == -1:
    print("debajo del peso ideal")
elif persona.calcularIMC() == 0:
    print("en su peso ideal")
else:
    print("Sobrepeso")