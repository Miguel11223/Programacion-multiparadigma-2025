"""
Modulo que se encarga del manejo de la biblioteca.
"""

import sys
from modelo import Biblioteca
from operacion import agregar_libro, agregar_usuario, prestar_libro, devolver_libro

def main():
    """
    Funcion que inicia la biblioteca y maneja el menú.

    No recibe parametros ni devuelve alguno, se repite en un ciclo del meno 
    """
    biblioteca = Biblioteca()

    while True:
        print("\nBiblioteca")
        print("1. Agregar libro")
        print("2. Agregar usuario")
        print("3. Mostrar libros disponibles")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Salir")

        try:
            opcion = int(input("Elige una opción (1-6): ").strip())
        except ValueError:
            print("Ingresa algun numero.")
            continue

        if opcion == 1:
            titulo = input("Titulo: ").strip()
            autor = input("Autor: ").strip()
            try:
                ano = int(input("Año: ").strip())
            except ValueError:
                print("El año no es valido. No se agregó el libro.")
                continue
            agregar_libro(biblioteca, titulo, autor, ano)
            print("Libro agregado.")

        elif opcion == 2:
            nombre = input("Nombre del usuario: ").strip()
            agregar_usuario(biblioteca, nombre)
            print("Usuario agregado.")

        elif opcion == 3:
            ()

        elif opcion == 4:
            usuario_nombre = input("Nombre del usuario: ").strip()
            titulo_libro = input("Libro a prestar: ").strip()
            if prestar_libro(biblioteca, usuario_nombre, titulo_libro):
                print("Libro prestado.")
            else:
                print("No se pudo hacer el prestamo.")

        elif opcion == 5:
            usuario_nombre = input("Nombre del usuario: ").strip()
            titulo_libro = input("Libro a devolver: ").strip()
            if devolver_libro(biblioteca, usuario_nombre, titulo_libro):
                print("Libro devuelto.")
            else:
                print("No se pudo hacer la devolucion.")

        elif opcion == 6:
            print("Que tenga buen dia .")
            sys.exit(0)

        else:
            print("Eso no es valido.")

if __name__ == "__main__":
    main()