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

class Inventario:
    def __init__(self):
        self.__productos = {}

    def agregar_producto(self, producto):
        self.__productos[producto.nombre] = producto

    def buscar_producto(self, nombre):
        return self.__productos.get(nombre)

    def total_valor_inventario(self):
        return sum(producto.precio * producto.stock for producto in self.__productos.values())

    def __len__(self):
        return len(self.__productos)

    def __str__(self):
        return "\n".join(str(producto) for producto in self.__productos.values())