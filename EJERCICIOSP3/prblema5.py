class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None  
        self.notas = []  
    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas:
            print(f"Notas: {', '.join(map(str, self.notas))}")
        else:
            print("Notas: No asignadas")
    def setAge(self, edad):
        if edad > 0:  
            self.edad = edad
        else:
            print("Error: La edad debe ser un número positivo.")

    def setNota(self, nota):
        if isinstance(nota, (int, float)): 
            self.notas.append(nota)
        else:
            print("Error: La nota debe ser un número.")

if __name__ == "__main__":
    alumno1 = Alumno("FABRIZZIO", "1510701023")
    alumno1.display()
    alumno1.setAge(20)
    alumno1.setNota(15)
    alumno1.setNota(17)
    alumno1.display()
