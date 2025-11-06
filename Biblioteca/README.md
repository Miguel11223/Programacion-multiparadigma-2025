# Sistema de Gestión de Biblioteca

## Descripción del Proyecto

Este proyecto es un sistema que se encarga de la gestión de una biblioteca que permite agregar libros y usuarios, mostrar los libros que esten disponibles, prestar y devolverlos.

Las clases principales son `Libro`, `Usuario` y `Biblioteca`.

## Instrucciones para Ejecutar el Programa

1. Ejecutar el comando: `python main.py` o darle  en ejecutar en visual studio code.
2. Dependiendo lo que se necesite realizar utilizar el menu ciclico a preferencia o necesidad.
3. Agregar Libro: En esta opcion se agrega un libro, Solicita: Título del libro, autor y año de publicación.
4. Agregar Usuario: En esta opcion se agregan los usuarios, Solicita: Nombre del usuario.
5. Mostrar Libros Disponibles: Muestra una lista numerada de libros que no están prestados.
6. Prestar Libro: Mediante los datos solicitados, hace la accion de prestar un libro y Solicita: Nombre del usuario y título del libro.
7. Devolver Libro: Mediante los datos solicitados, hace la accion de prestar un libro y Solicita: Nombre del usuario y título del libro.
8. En caso de querer salirse.

## Estructura del Código

El proyecto está organizado en módulos:

- **main.py**: Es el archivo principal que maneja el programa y utiliza funciones de otros módulos.
- **modelos.py**: Define las clases de entidad (`Libro`, `Usuario`, `Biblioteca`).
- **operaciones.py**: Contiene funciones para las operaciones que se pueden realizar en la biblioteca.
  