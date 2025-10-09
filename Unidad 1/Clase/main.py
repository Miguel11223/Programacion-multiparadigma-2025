from libro import Libro  # type: ignore

libro1 = Libro("El Quijote", "Miguel de Cervantes", 1605)
libro2 = Libro("1984", "George Orwell", 1949)
libro3 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)

libro1.prestar()
libro2.prestar()
libro2.devolver()
libro3.prestar()
libro3.devolver()
