class Persona:
    def __init__(self, nombre, apellido, dni, estadoCivil):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._estadoCivil = estadoCivil

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = dni

    @property
    def estadoCivil(self):
        return self._estadoCivil

    @estadoCivil.setter
    def estadoCivil(self, estadoCivil):
        self._estadoCivil = estadoCivil

    def __str__(self):
        return f"Persona: nombre: {self._nombre}, apellido: {self._apellido}, dni: {self._dni}, estado civil: {self._estadoCivil}"

class Empleado(Persona):
    def __init__(self, nombre, apellido, dni, estadoCivil, anioIncorp, numDespacho):
        super().__init__(nombre, apellido, dni, estadoCivil)
        self._anioIncorp = anioIncorp
        self._numDespacho = numDespacho

    @property
    def anioIncorp(self):
        return self._anioIncorp

    @anioIncorp.setter
    def anioIncorp(self, anioIncorp):
        self._anioIncorp = anioIncorp

    @property
    def numDespacho(self):
        return self._numDespacho

    @numDespacho.setter
    def numDespacho(self, numDespacho):
        self._numDespacho = numDespacho

    def __str__(self):
        return f"{super().__str__()}, Empleado: año de incorporacion: {self._anioIncorp}, Numero de despacho: {self._numDespacho}"

class Estudiante(Persona):
    def __init__(self, nombre, apellido, dni, estadoCivil, curso):
        super().__init__(nombre, apellido, dni, estadoCivil)
        self._curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        self._curso = curso

    def __str__(self):
        return f"{super().__str__()}, Estudiante: Curso: {self._curso}"

class Profesor(Empleado):
    def __init__(self, nombre, apellido, dni, estadoCivil, anioIncorp, numDespacho, depto):
        super().__init__(nombre, apellido, dni, estadoCivil, anioIncorp, numDespacho)
        self._depto = depto

    @property
    def depto(self):
        return self._depto

    @depto.setter
    def depto(self, depto):
        self._depto = depto

    def __str__(self):
        return f"{super().__str__()}, Profesor: Departamento {self._depto}"

class PersonalServicio(Empleado):
    def __init__(self, nombre, apellido, dni, estadoCivil, anioIncorp, numDespacho, seccion):
        super().__init__(nombre, apellido, dni, estadoCivil, anioIncorp, numDespacho)
        self._seccion = seccion

    @property
    def seccion(self):
        return self._seccion

    @seccion.setter
    def seccion(self, seccion):
        self._seccion = seccion

    def __str__(self):
        return f"{super().__str__()}, Personal de Servicio: Seccion: {self._seccion}"

servi = PersonalServicio("Damian", "Lobos", 38607219, "Casado", 2021, 3, 5)
print(servi)