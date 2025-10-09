# -*- coding: utf-8 -*-
from libro import Libro  
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

libro1 = Libro("El Quijote", "Miguel de Cervantes", 1605)
libro2 = Libro("1984", "George Orwell", 1949)
libro3 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)

libros = [libro1, libro2, libro3]  

def menu():
    while True:
        print("\n--- Menú de Biblioteca ---")
        print("1. Mostrar estado de todos los libros")
        print("2. Prestar un libro")
        print("3. Devolver un libro")
        print("4. Salir")
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == "1":
            for libro in libros:
                libro.mostrar_estado()
        elif opcion == "2":
            prestar_libro()
        elif opcion == "3":
            devolver_libro()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

def prestar_libro():
    print("\nLibros disponibles para prestar:")
    disponibles = [libro for libro in libros if not libro.prestado]
    if not disponibles:
        print("No hay libros disponibles para prestar.")
        return
    for i, libro in enumerate(disponibles, 1):
        print(f"{i}. {libro.titulo} por {libro.autor}")
    try:
        eleccion = int(input("Elige el número del libro a prestar (o 0 para cancelar): "))
        if eleccion == 0:
            return
        if 1 <= eleccion <= len(disponibles):
            disponibles[eleccion - 1].prestar()
        else:
            print("Elección inválida.")
    except ValueError:
        print("Entrada inválida. Debe ser un número.")

def devolver_libro():
    print("\nLibros prestados para devolver:")
    prestados = [libro for libro in libros if libro.prestado]
    if not prestados:
        print("No hay libros prestados para devolver.")
        return
    for i, libro in enumerate(prestados, 1):
        print(f"{i}. {libro.titulo} por {libro.autor}")
    try:
        eleccion = int(input("Elige el número del libro a devolver (o 0 para cancelar): "))
        if eleccion == 0:
            return
        if 1 <= eleccion <= len(prestados):
            prestados[eleccion - 1].devolver()
        else:
            print("Elección inválida.")
    except ValueError:
        print("Entrada inválida. Debe ser un número.")

menu()