class Libro:
    biblioteca = "Biblioteca Central"

    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.prestado = False

    def prestar(self):
        self.prestado = True
        print(f"El libro {self.titulo} ha sido prestado.")

    def devolver(self):
        self.prestado = False
        print(f"El libro {self.titulo} ha sido devuelto.")

    def mostrar_estado(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.anio_publicacion}")
        print(f"Prestado: {'Sí' if self.prestado else 'No'}")
        print(f"Biblioteca: {self.biblioteca}")
        print()