# Proyecto Biblioteca: Modelo de Libros en Python

Este es un proyecto simple en Python que modela un libro en una biblioteca usando programación orientada a objetos (POO). Incluye una clase `Libro` y un script principal (`main.py`) para demostrar su uso de manera interactiva a través de un menú.

## Estructura del Proyecto

- **libro.py**: Contiene la definición de la clase `Libro` .
- **main.py**: Script principal que  presenta un menú interactivo para prestar, devolver y mostrar el estado de los libros.
- **README.md**: Este archivo con documentación.

## Explicación del Diseño

La clase `Libro` está diseñada para representar un libro en un sistema de biblioteca básico, siguiendo principios de POO como encapsulación y simplicidad. Aquí va una explicación breve de por qué elegí estos atributos y métodos:

### Atributos de Instancia

- `titulo` (str): Representa el nombre del libro. Elegido porque es el identificador principal y único para cada instancia.
- `autor` (str): Almacena el nombre del autor.
- `anio_publicacion` (int): Indica el año de publicación.
- `prestado` (bool, inicializado en False): Rastrea si el libro está prestado.

Estos atributos cubren los aspectos básicos de un libro en una biblioteca.

### Atributo de Clase

- `biblioteca` (str = "Biblioteca Central"): Compartido por todos los libros, representa la biblioteca propietaria..

### Métodos

- `__init__`: Inicializa los atributos de instancia. Estándar en POO para crear objetos con datos específicos.
- `prestar()`: Cambia `prestado` a True e imprime un mensaje. Elegido para simular el préstamo.
- `devolver()`: Cambia `prestado` a False e imprime un mensaje. Similar al anterior, para manejar la devolución y mantener consistencia.
- `mostrar_estado()`: Imprime todos los detalles del libro, incluyendo si está prestado y la biblioteca.

El diseño prioriza simplicidad y legibilidad: métodos cortos, nombres descriptivos.

## Ejecución en Consola

Para ejecutar el proyecto:

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta: `python main.py`.

El programa presenta un menú interactivo donde puedes:

- Mostrar el estado de todos los libros.
- Prestar un libro (elige de los disponibles).
- Devolver un libro (elige de los prestados).
- Salir.
