
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
        Se encarga de inicialzar un libro 

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