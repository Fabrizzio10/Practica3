import math
class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)
def obtener_radio():
    while True:
        try:
            radio = float(input("Ingrese el radio del círculo: "))
            if radio <= 0:
                print("El radio debe ser un número positivo.")
            else:
                return radio
        except ValueError:
            print("Error: Debes ingresar un número válido.")

radio1 = obtener_radio()
circulo1 = CIRCULO(radio1)

radio2 = obtener_radio()
circulo2 = CIRCULO(radio2)

print(f"El área del círculo 1 con radio {radio1} es: {circulo1.calcular_area():.2f}")
print(f"El área del círculo 2 con radio {radio2} es: {circulo2.calcular_area():.2f}")