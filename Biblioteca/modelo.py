
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



        def agregar_libro(self, titulo, autor, ano):
        libro = Libro(titulo, autor, ano)
        self.libros.append(libro)
        return libro

    def agregar_usuario(self, nombre):
        usuario = Usuario(nombre)
        self.usuarios.append(usuario)
        return usuario

    def listar_libros_disponibles(self):
        disponibles = [libro for libro in self.libros if libro.disponible]
        return disponibles

    def prestar_libro(self, usuario_nombre, titulo_libro):
        usuario = next((u for u in self.usuarios if u.nombre == usuario_nombre), None)
        if not usuario:
            return False
        libro = next((l for l in self.libros if l.titulo == titulo_libro and l.disponible), None)
        if not libro:
            return False
        libro.disponible = False
        usuario.libros_prestados.append(libro)
        return True

    def devolver_libro(self, usuario_nombre, titulo_libro):
        usuario = next((u for u in self.usuarios if u.nombre == usuario_nombre), None)
        if not usuario:
            return False
        libro = next((l for l in usuario.libros_prestados if l.titulo == titulo_libro), None)
        if not libro:
            return False
        libro.disponible = True
        usuario.libros_prestados.remove(libro)
        return True



# Prueba
if __name__ == "__main__":
    bib = Biblioteca()
    bib.agregar_libro("1984", "George Orwell", 1949)
    bib.agregar_usuario("Alice")
    bib.prestar_libro("Alice", "1984")
    disponibles = bib.listar_libros_disponibles()
    print(f"Libros disponibles: {len(disponibles)}")
    bib.devolver_libro("Alice", "1984")
    disponibles = bib.listar_libros_disponibles()
    print(f"Libros disponibles después de devolver: {len(disponibles)}")