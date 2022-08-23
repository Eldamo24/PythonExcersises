from Coche import Coche
from Camioneta import Camioneta
from Bicicleta import Bicicleta
from Motocicleta import Motocicleta

def catalogar(vehiculos):
    for vehiculo in vehiculos:
        print("\n")
        print(type(vehiculo).__name__)  #Devuelve nombre de la clase
        vehiculo.toString()


coche = Coche("Negro", 4, 150, 250)
camioneta = Camioneta("Negro", 4, 150, 250, 500)
bici = Bicicleta("Verde", 2, "Urbana")
moto = Motocicleta("Marron", 2, "Deportiva", 200, 500)
vehiculos = [coche, camioneta, bici, moto]
catalogar(vehiculos)


