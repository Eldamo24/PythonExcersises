class Libro:
    def __init__(self, isbn = 0, titulo = "", autor = "", numPags = 0):
        self._isbn = isbn
        self._titulo = titulo
        self._autor = autor
        self._numPags = numPags

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, isbn):
        self._isbn = isbn

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @property
    def numPags(self):
        return self._numPags

    @numPags.setter
    def numPags(self, numPags):
        self._numPags = numPags

    def toString(self):
        print(f"ISBN: {self._isbn} \nTitulo: {self._titulo} \nAutor: {self._autor} \nNumero de paginas: {self._numPags}")

def cargarLibro():
    isbn = int(input("Ingrese isbn: "))
    autor = input("Ingrese autor del libro: ")
    titulo = input("Ingrese titulo del libro: ")
    numPags = int(input("Ingrese cantidad de paginas del libro: "))
    return Libro(isbn, titulo, autor, numPags)

libro = cargarLibro()
libro.toString()