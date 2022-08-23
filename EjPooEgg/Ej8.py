import random
import math

class Matematica:
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    @property
    def num1(self):
        return self._num1

    @num1.setter
    def num1(self, num1):
        self._num1 = num1

    @property
    def num2(self):
        return self._num2

    @num2.setter
    def num2(self, num2):
        self._num2 = num2

    def mayor(self):
        if self._num1 >= self._num2:
            return self._num1
        else:
            return self._num2

    def elevar(self, num):
        if num == self._num1:
            return self._num1 ** self._num2
        else:
            return self._num2 ** self._num1

    def raiz(self, num):
        if num == self._num1:
            return math.sqrt(self._num2)
        else:
            return math.sqrt(self._num1)

    def __str__(self):
        return f"num1: {self._num1}, num2: {self._num2}"

def crearMate():
    return Matematica(random.randint(1,50), random.randint(1,50))

mate = crearMate()
print(mate)
print(f"El mayor es: {mate.mayor()}")
print(f"El mayor elevado al menor: {mate.elevar(mate.mayor())}")
print(f"Raiz cuadrada del menor: {mate.raiz(mate.mayor())}")
