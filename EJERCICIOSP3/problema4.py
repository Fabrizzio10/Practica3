class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    def calcular_area(self):
        return self.largo * self.ancho
class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        super().__init__(lado, lado)
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

largo = obtener_numero("Ingrese el largo del rectángulo: ")
ancho = obtener_numero("Ingrese el ancho del rectángulo: ")
lado_cuadrado = obtener_numero("Ingrese el lado del cuadrado: ")

rectangulo = RECTANGULO(largo, ancho)
cuadrado = CUADRADO(lado_cuadrado)

print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
print(f"El área del cuadrado es: {cuadrado.calcular_area()}")
