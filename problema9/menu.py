from formulas import CIRCULO, RECTANGULO, CUADRADO

def obtener_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("Por favor, ingrese un número positivo.")
            else:
                return valor
        except ValueError:
            print("Error: Debes ingresar un número válido.")

def mostrar_menu():
    print("\n--- Menú de Opciones ---")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado")
    print("4. Salir")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            radio = obtener_numero("Ingrese el radio del círculo: ")
            circulo = CIRCULO(radio)
            print(f"El área del círculo es: {circulo.calcular_area():.2f}")

        elif opcion == "2":
            largo = obtener_numero("Ingrese el largo del rectángulo: ")
            ancho = obtener_numero("Ingrese el ancho del rectángulo: ")
            rectangulo = RECTANGULO(largo, ancho)
            print(f"El área del rectángulo es: {rectangulo.calcular_area():.2f}")

        elif opcion == "3":
            lado = obtener_numero("Ingrese el lado del cuadrado: ")
            cuadrado = CUADRADO(lado)
            print(f"El área del cuadrado es: {cuadrado.calcular_area():.2f}")

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

# Ejecutar el menú
if __name__ == "__main__":
    ejecutar_menu()
