
'''
Es modulo que se encarga de definir las clases para el modelado de datos de la biblioteca
Este incluye Libro, Usuario y biblioteca 
'''
class Libro: 
    """
    Es la clase que representa al libro  
    
    Atributos
        titulo (str): titulo del libro.
        autor (str): autor del libro.
        ano (int): año de publicación.
        disponible (bool): True en caso de estar disponible 
    """
    def __init__(self, titulo, autor, ano):
        """
        Se encarga de inicializar un libro 

        Parametros: 
            titulo (str): Título.
            autor (str): Autor.
            ano (int): Año.

        No devuelve valores 
        """
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponible = True

class Usuario:
    """
    Es la clase que representa al usuario

    Atributos:
        nombre (str): Nombre del usuario
        libros_prestados (list): Lista de Libros 
    """
    def __init__(self, nombre):
        """
        Inicializa un usuario

        Parámetros:
            nombre (str): Nombre

        No devuelve valores
        """
        self.nombre = nombre
        self.libros_prestados = []

class Biblioteca:
    """
    Clase que se encarga de gestionar libros y usuarios

    Atributos:
        libros (list): Lista de los libros
        usuarios (list): Lista de los usuarios
    """
    def __init__(self):
        """
        Inicializa la biblioteca.

        No recibe ni devuelve parametros de algun tipo 
        """
        self.libros = []
        self.usuarios = []