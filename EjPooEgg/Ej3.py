class Operacion:
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

    def suma(self):
        return self._num1 + self._num2

    def resta(self):
        return self._num1 - self._num2

    def multi(self):
        if self._num2 == 0 or self._num1 == 0:
            return 0
        else:
            return self._num1 * self._num2

    def division(self):
        if self._num2 == 0:
            return 0
        else:
            return self._num1 / self._num2



def crearOperacion():
    num1 = float(input("Ingrese un numero: "))
    num2 = float(input("Ingrese otro numero: "))
    return Operacion(num1, num2)

op = crearOperacion()
print(op.suma())
print(op.resta())
print(op.multi())
print(op.division())