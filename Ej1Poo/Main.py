from Persona import Persona

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
dni = int(input("Ingrese su numero de documento: "))

persona1 = Persona(nombre, edad, dni)
persona1.toString()
print(f"{persona1.nombre} es mayor de edad?: " + str(persona1.esMayor()))