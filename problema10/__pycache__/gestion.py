from libro import Libro

class GestionBiblioteca:
    def __init__(self):
        self.libros = []  # Lista de libros

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def listar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            for libro in self.libros:
                print(libro)

    def buscar_por_titulo(self, titulo):
        libros_encontrados = [libro for libro in self.libros if libro.titulo.lower() == titulo.lower()]
        return libros_encontrados

    def buscar_por_autor(self, autor):
        libros_encontrados = [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
        return libros_encontrados
    