"""Crea una clase llamada Cuenta que tendrá los siguientes atributos:
titular (que es una persona) y cantidad (puede tener decimales).
El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
mostrar(): Muestra los datos de la cuenta.
ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos."""

class Cuenta:
    def __init__(self, titular, cantidad = 0):
        self._titular = titular
        self._cantidad = cantidad

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

    def toString(self):
        print(f"Titular: {self._titular} \nCantidad: {self._cantidad}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("No puedes retirar un saldo negativo o igual a cero")
        else:
            if cantidad > self._cantidad:
                self._cantidad = 0
            else:
                self._cantidad -= cantidad

