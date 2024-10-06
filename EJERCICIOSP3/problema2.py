def calificaciones():
    while True:
        try:
            x = input("Ingrese una lista de calificaciones separadas por comas: ")
            lista = x.split(',')
            lista_enteros = [int(cal) for cal in lista]
            return lista_enteros
        
        except ValueError:
            print("Error: Asegúrate de ingresar solo números enteros separados por comas.")
        
if __name__ == "__main__":
    x = calificaciones()
    print(f"Las calificaciones ingresadas son: {calificaciones}")
