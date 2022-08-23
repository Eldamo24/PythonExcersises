from Cuenta import Cuenta

titular = input("Ingrese nombre del titular de la cuenta: ")
cantidad = float(input("Ingrese saldo a la cuenta: "))

cuenta1 = Cuenta(titular, cantidad)
cuenta1.toString()
cuenta1.ingresar(3500)
cuenta1.toString()
cuenta1.retirar(10000)
cuenta1.toString()