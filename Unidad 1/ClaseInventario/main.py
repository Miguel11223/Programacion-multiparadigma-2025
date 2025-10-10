from producto import Producto, Inventario

def main():
    inventario = Inventario()

    laptop = Producto("Laptop", 1000.0)
    mouse = Producto("Mouse", 20.0)
    teclado = Producto("Teclado", 50.0)
    monitor = Producto("Monitor", 200.0)

    laptop.stock = 10
    laptop.precio = 1200.0
    mouse.stock = 50
    teclado.stock = 30
    monitor.stock = 15

    inventario.agregar_producto(laptop)
    inventario.agregar_producto(mouse)
    inventario.agregar_producto(teclado)
    inventario.agregar_producto(monitor)

    print("\nProductos disponibles para comparar:")
    print(", ".join([producto.nombre for producto in inventario._Inventario__productos.values()]))
    nombre1 = input("Ingrese el nombre del primer producto a comparar: ")
    nombre2 = input("Ingrese el nombre del segundo producto a comparar: ")

    producto1 = inventario.buscar_producto(nombre1)
    producto2 = inventario.buscar_producto(nombre2)

    if producto1 and producto2:
        print(f"\n¿Son iguales los productos {nombre1} y {nombre2}? {producto1 == producto2}")
    else:
        print("\nUno o ambos productos no se encontraron en el inventario.")

        

