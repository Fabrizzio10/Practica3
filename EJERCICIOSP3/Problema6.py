class Producto:
    def __init__(self, nombre, precio, ano):
        self.nombre = nombre
        self.precio = precio
        self.ano = ano

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: ${self.precio:.2f}, Año: {self.ano}"

class Catalogo:
    def __init__(self):
        self.productos = []  
        
    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if not self.productos:
            print("El catálogo está vacío.")
        else:
            print("Lista de Productos:")
            for producto in self.productos:
                print(producto)

    def filtrar_por_ano(self, ano):
        productos_filtrados = [producto for producto in self.productos if producto.ano == ano]
        if productos_filtrados:
            print(f"Productos del año {ano}:")
            for producto in productos_filtrados:
                print(producto)
        else:
            print(f"No hay productos del año {ano}.")

    def filtrar_por_precio(self, precio_maximo):
        productos_filtrados = [producto for producto in self.productos if producto.precio <= precio_maximo]
        if productos_filtrados:
            print(f"Productos con precio hasta ${precio_maximo:.2f}:")
            for producto in productos_filtrados:
                print(producto)
        else:
            print(f"No hay productos con precio hasta ${precio_maximo:.2f}.")

if __name__ == "__main__":
  
    catalogo = Catalogo()

 
    producto1 = Producto("Batería", 150.00, 2022)
    producto2 = Producto("Frenos", 80.50, 2021)
    producto3 = Producto("Aceite de motor", 25.00, 2023)

    # Agregar productos al catálogo
    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)

    # Mostrar todos los productos
    catalogo.mostrar_productos()

    # Filtrar productos por año
    catalogo.filtrar_por_ano(2022)

    # Filtrar productos por precio
    catalogo.filtrar_por_precio(100.00)
