class CuentaBancaria:

    _id = 0 #Variable de clase

    @classmethod
    def _incrementoId(cls):
        cls._id += 1
        return cls._id

    def __init__(self, dni, saldo):
        self._numCuenta = CuentaBancaria._incrementoId()
        self._dni = dni
        self._saldo = saldo

    @property
    def numCuenta(self):
        return self._numCuenta

    @numCuenta.setter
    def numCuenta(self, numCuenta):
        self._numCuenta = numCuenta

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = dni

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    def ingresarSaldo(self, saldo):
        if saldo > 0:
            self._saldo += saldo

    def retirarSaldo(self, retiro):
        if retiro >= self._saldo:
            self._saldo = 0
        else:
            self._saldo -= retiro

    def extraccionRapida(self, retiro):
        porcentaje = 20 * self._saldo / 100
        if retiro <= porcentaje:
            self._saldo -= retiro
        else:
            print("No puedes extraer esa cantidad con extracciones rapidas...")

    def __str__(self):
        return f"Cuenta: Numero de cuenta: {self._numCuenta}, DNI: {self._dni}, Saldo: {self._saldo}"

def crearCuenta():
    dni = int(input("Ingrese su dni: "))
    saldo = float(input("Ingrese el saldo de su cuenta: "))
    return CuentaBancaria(dni, saldo)

cuenta = crearCuenta()
print(cuenta)
cuenta.ingresarSaldo(10000)
print(cuenta)
cuenta.retirarSaldo(15000)
print(cuenta)
cuenta.extraccionRapida(50000)
print(cuenta)