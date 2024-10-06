from gestion import GestionBiblioteca
from libro import Libro

def mostrar_menu():
    print("\n--- Menú de Gestión de Biblioteca ---")
    print("1. Agregar un libro a nuestra biblioteca")
    print("2. Listar los libros en nuestra biblioteca")
    print("3. Buscar un libro según su título")
    print("4. Buscar un libro según su autor")
    print("5. Salir")

def ejecutar_menu():
    gestion = GestionBiblioteca()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, isbn)
            gestion.agregar_libro(libro)
            print("Libro agregado exitosamente.")

        elif opcion == "2":
            print("Libros en la biblioteca:")
            gestion.listar_libros()

        elif opcion == "3":
            titulo = input("Ingrese el título del libro a buscar: ")
            libros_encontrados = gestion.buscar_por_titulo(titulo)
            if libros_encontrados:
                for libro in libros_encontrados:
                    print(libro)
            else:
                print("No se encontraron libros con ese título.")

        elif opcion == "4":
            autor = input("Ingrese el autor del libro a buscar: ")
            libros_encontrados = gestion.buscar_por_autor(autor)
            if libros_encontrados:
                for libro in libros_encontrados:
                    print(libro)
            else:
                print("No se encontraron libros de ese autor.")

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    ejecutar_menu()