"""
Es el modulo en el cual se realizan funciones para interactuar con la biblioteca
Este incluye agregar, listar prestar y devolver
"""
from modelo import Libro, Usuario

def agregar_libro(biblioteca, titulo, autor, ano):
    """
    Agrega libros

    Parámetros:
        biblioteca (Biblioteca): instancia
        titulo (str): título
        autor (str): autor
        ano (int): año

    No devuelve valores
    """
    libro = Libro(titulo, autor, ano)
    biblioteca.libros.append(libro)

def agregar_usuario(biblioteca, nombre):
    """
    Agrega usuarios 

    Parámetros:
        biblioteca (Biblioteca): Instancia
        nombre (str): Nombre

    No devuelve valores
    """
    usuario = Usuario(nombre)
    biblioteca.usuarios.append(usuario)

def listar_libros_disponibles(biblioteca):
    """
    Lista libros disponibles

    Parámetros:
        biblioteca (Biblioteca): Instancia

    Devuelve:
        list: Libros que hay disponibles
    """
    return [libro for libro in biblioteca.libros if libro.disponible]

def prestar_libro(biblioteca, usuario_nombre, titulo_libro):
    """
    Presta algun libro

    Parámetros:
        biblioteca (Biblioteca): Instancia
        usuario_nombre (str): Nombre del usuario
        titulo_libro (str): Título del libro

    Devuelve:
        bool: True si funciona bien  
    """
    usuario = next((u for u in biblioteca.usuarios if u.nombre == usuario_nombre), None)
    if not usuario:
        return False
    libro = next((l for l in biblioteca.libros if l.titulo == titulo_libro and l.disponible), None)
    if not libro:
        return False
    libro.disponible = False
    usuario.libros_prestados.append(libro)
    return True

def devolver_libro(biblioteca, usuario_nombre, titulo_libro):
    """
    Devuelve algun libro

    Parámetros:
        biblioteca (Biblioteca): Instancia
        usuario_nombre (str): Nombre usuario
        titulo_libro (str): Título libro

    Retorna:
        bool: True si funciona bien 
    """
    usuario = next((u for u in biblioteca.usuarios if u.nombre == usuario_nombre), None)
    if not usuario:
        return False
    libro = next((l for l in usuario.libros_prestados if l.titulo == titulo_libro), None)
    if not libro:
        return False
    libro.disponible = True
    usuario.libros_prestados.remove(libro)
    return True