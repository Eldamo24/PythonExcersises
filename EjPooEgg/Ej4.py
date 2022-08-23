class Rectangulo:
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        self._base = base

    @property
    def altura(self):
        return self._altura

    @base.setter
    def altura(self, altura):
        self._altura = altura

    def __str__(self):
        return f"Rectangulo: Base {self._base}, Altura: {self._altura}"

    def area(self):
        return self._base * self._altura

    def perimetro(self):
        return (self._base + self._altura) * 2

    def dibujarRect(self):
        for i in range(int(self._altura)):
            for j in range(int(self._base)):
                print("*", end ="")
            print("\n")

def crearRect():
    base = float(input("Ingrese base del rectangulo: "))
    altura = float(input("Ingrese altura del rectangulo: "))
    return Rectangulo(base, altura)

rect = crearRect()
print(rect.area())
print(rect.perimetro())
rect.dibujarRect()
