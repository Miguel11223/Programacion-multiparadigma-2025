from producto import Producto, Inventario

def mostrar_menu():
    print("\n=== Menú de Inventario ===")
    print("1. Mostrar inventario")
    print("2. Mostrar valor total del inventario")
    print("3. Buscar producto")
    print("4. Modificar stock de un producto")
    print("5. Modificar precio de un producto")
    print("6. Comparar dos productos")
    print("7. Salir")

def main():
    inventario = Inventario()

    try:
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
    except ValueError as e:
        print(f"Error al inicializar productos: {e}")
        return

    