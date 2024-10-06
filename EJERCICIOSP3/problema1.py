def obtener_fraccion():
    while True:
        try:
            fraccion = input("Ingrese la fracción (formato X/Y): ")
            x, y = fraccion.split('/')
            x = int(x)
            y = int(y)
        
            if y == 0:
                raise ZeroDivisionError
            
            if x > y:
                raise ValueError
            porcentaje = (x / y) * 100
        
            if porcentaje <= 1:
                return "E"
            elif porcentaje >= 99:
                return "F"
            else:
                return f"{round(porcentaje)}%"
        
        except ValueError:
            print("Error: Debes ingresar dos números enteros válidos.")
        except ZeroDivisionError:
            print("Error: El denominador no puede ser 0.")

if __name__ == "__main__":
    resultado = obtener_fraccion()
    print(f"Resultado: {resultado}")