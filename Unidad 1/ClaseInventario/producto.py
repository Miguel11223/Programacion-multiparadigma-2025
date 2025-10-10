class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.__stock = 0
        self._precio = precio if precio > 0 else ValueError("El precio debe ser mayor a 0")

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise ValueError("El stock no puede ser menor a 0")
        self.__stock = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        self._precio = valor

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: ${self._precio}, Stock: {self.__stock}"

    def __eq__(self, other):
        if isinstance(other, Producto):
            return self.nombre == other.nombre
        return False