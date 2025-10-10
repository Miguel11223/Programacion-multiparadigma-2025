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
