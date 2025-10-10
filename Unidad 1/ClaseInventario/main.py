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

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-7): ").strip()

        if opcion == "1":
            print("\nInventario:")
            print(inventario)

        elif opcion == "2":
            print(f"\nValor total del inventario: ${inventario.total_valor_inventario()}")

        elif opcion == "3":
            nombre = input("\nIngrese el nombre del producto a buscar: ").strip()
            producto_buscado = inventario.buscar_producto(nombre)
            print(f"\nProducto buscado: {producto_buscado if producto_buscado else 'No encontrado'}")

        elif opcion == "4":
            print("\nProductos disponibles:")
            print(", ".join([producto.nombre for producto in inventario._Inventario__productos.values()]))
            nombre = input("Ingrese el nombre del producto: ").strip()
            producto = inventario.buscar_producto(nombre)
            if producto:
                try:
                    nuevo_stock = int(input(f"Ingrese el nuevo stock para {nombre}: "))
                    producto.stock = nuevo_stock
                    print(f"Stock de {nombre} actualizado a {producto.stock}")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print(f"\nProducto {nombre} no encontrado.")

        elif opcion == "5":
            print("\nProductos disponibles:")
            print(", ".join([producto.nombre for producto in inventario._Inventario__productos.values()]))
            nombre = input("Ingrese el nombre del producto: ").strip()
            producto = inventario.buscar_producto(nombre)
            if producto:
                try:
                    nuevo_precio = float(input(f"Ingrese el nuevo precio para {nombre}: "))
                    producto.precio = nuevo_precio
                    print(f"Precio de {nombre} actualizado a ${producto.precio}")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print(f"\nProducto {nombre} no encontrado.")

        elif opcion == "6":
            print("\nProductos disponibles para comparar:")
            print(", ".join([producto.nombre for producto in inventario._Inventario__productos.values()]))
            nombre1 = input("Ingrese el nombre del primer producto a comparar: ").strip()
            nombre2 = input("Ingrese el nombre del segundo producto a comparar: ").strip()

            producto1 = None
            producto2 = None
            for producto in inventario._Inventario__productos.values():
                if producto.nombre.lower() == nombre1.lower():
                    producto1 = producto
                if producto.nombre.lower() == nombre2.lower():
                    producto2 = producto

            if producto1 and producto2:
                print(f"\n¿Son iguales los productos {producto1.nombre} y {producto2.nombre}? {producto1 == producto2}")
            else:
                print("\nUno o ambos productos no se encontraron en el inventario.")

        elif opcion == "7":
            print("\nPrograma finalizado.")
            break

        else:
            print("\nOpción no válida, por favor seleccione una opción entre 1 y 7.")

if __name__ == "__main__":
    main()