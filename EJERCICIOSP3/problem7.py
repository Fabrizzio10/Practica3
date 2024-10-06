import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "Origen"
        elif self.x == 0:
            return "Eje Y"
        elif self.y == 0:
            return "Eje X"
        elif self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
    
    def vector(self, otro_punto):
        return (otro_punto.x - self.x, otro_punto.y - self.y)

    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)

class Rectangulo:
    def __init__(self, punto1=Punto(), punto2=Punto()):
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        return abs(self.punto2.x - self.punto1.x)

    def altura(self):
        return abs(self.punto2.y - self.punto1.y)

    def area(self):
        return self.base() * self.altura()

A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)
print(f"A: {A} está en el {A.cuadrante()}")
print(f"B: {B} está en el {B.cuadrante()}")
print(f"C: {C} está en el {C.cuadrante()}")
print(f"D: {D} está en el {D.cuadrante()}")

print(f"Vector AB: {A.vector(B)}")
print(f"Distancia entre A y B: {A.distancia(B)}")

rectangulo = Rectangulo(A, B)
print(f"Base: {rectangulo.base()}, Altura: {rectangulo.altura()}, Área: {rectangulo.area()}")