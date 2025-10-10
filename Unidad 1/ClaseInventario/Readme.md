# Sistema de Gestión de Inventario

Descripción
Este proyecto implementa un sistema de gestión de inventario que incluye dos clases principales: Producto para representar productos individuales y Inventario para gestionar una colección de productos. El sistema permite crear productos, modificar sus atributos (stock y precio), buscar productos, calcular el valor total del inventario y comparar productos por nombre, todo con una interfaz interactiva en main.py.
Estructura del Proyecto

producto.py: Contiene las clases Producto e Inventario con sus definiciones y métodos.
main.py: Script principal que inicializa un inventario, crea productos, y ofrece un menú para gestionar el inventario y comparar productos.
README.md: Este archivo, que explica el diseño y las decisiones tomadas.

Decisiones de Diseño

1. Encapsulación con Atributos Privados y Getters/Setters
La encapsulación se implementó para proteger los datos internos de las clases y garantizar un acceso controlado, siguiendo principios de POO:

Atributos Privados y Protegidos:

En la clase Producto:
__stock (privado): El stock se marcó como privado para evitar modificaciones directas que podrían violar la restricción de no permitir valores negativos. Solo se puede acceder o modificar a través de los métodos getter y setter.
_precio (protegido): El precio se marcó como protegido para permitir acceso en posibles clases derivadas (herencia futura), pero se controla mediante getters y setters para validar que sea mayor a 0.
nombre (público): Como el nombre no requiere validaciones estrictas y es un identificador clave, se dejó público para simplificar el acceso.

En la clase Inventario:
__productos (privado): El diccionario que almacena los productos se marcó como privado para evitar modificaciones directas en la estructura de datos, asegurando que todas las operaciones (agregar, buscar) pasen por los métodos definidos.

Getters y Setters:

Para Producto.stock y Producto.precio, se usaron decoradores @property (getter) y @<prop>.setter para proporcionar acceso controlado:
Getter de stock: Retorna el valor de __stock sin exponerlo directamente.
Setter de stock: Valida que el valor no sea menor a 0, lanzando un ValueError si no cumple.
Getter de precio: Retorna el valor de _precio.
Setter de precio: Valida que el valor sea mayor a 0, lanzando un ValueError si no cumple.

Esto asegura que las validaciones se apliquen consistentemente y protege la integridad de los datos.

1. Abstracción Aplicada
La abstracción se utilizó para simplificar la interacción con las clases, exponiendo solo las funcionalidades necesarias y ocultando los detalles internos:

Clase Producto:

Abstracción de un producto: Representa un producto con atributos esenciales (nombre, precio, stock) y métodos para gestionarlos. Los usuarios interactúan con el objeto a través de métodos como __str__ (para mostrar información) y __eq__ (para comparar por nombre), sin necesidad de conocer cómo se almacenan o validan los datos internamente.
Métodos especiales:
__str__: Proporciona una representación legible del producto (e.g., "Nombre: Laptop, Precio: $1200.0, Stock: 10"), abstrayendo los detalles de formato.
__eq__: Compara productos por nombre, simplificando la lógica de comparación para el usuario.

Validaciones internas: Las restricciones (stock ≥ 0, precio > 0) se manejan internamente, permitiendo al usuario enfocarse en la funcionalidad sin preocuparse por los detalles de implementación.

Clase Inventario:

Abstracción de la colección: Representa el inventario como un diccionario de productos, pero los usuarios solo interactúan a través de métodos como agregar_producto, buscar_producto, total_valor_inventario, __len__ y __str__.
Métodos especiales:
__len__: Devuelve el número de productos, abstrayendo la necesidad de acceder al diccionario __productos.
__str__: Muestra todos los productos en un formato legible, sin exponer la estructura interna del diccionario.

Operaciones simplificadas:
agregar_producto: Permite agregar o actualizar productos sin que el usuario manipule el diccionario directamente.
buscar_producto: Retorna un producto o None, ocultando la lógica de búsqueda en el diccionario.
total_valor_inventario: Calcula el valor total (precio * stock) iterando internamente sobre los productos, sin exponer esta lógica al usuario.

Beneficios de la Abstracción:

Simplicidad: Los usuarios interactúan con interfaces claras (métodos y propiedades) sin necesidad de entender la implementación interna.
Flexibilidad: Cambios en la estructura interna (e.g., cambiar el diccionario por una lista) no afectarían el código que usa la clase.
Reusabilidad: Las clases pueden integrarse en otros sistemas sin requerir que el usuario comprenda los detalles.

3. Interfaz Interactiva (main.py)
El script principal ofrece un menú interactivo que aprovecha los métodos de las clases:

Creación inicial: Crea un inventario con 4 productos, usando setters para inicializar stock y precios con validaciones.
Funcionalidades:
Muestra el inventario completo.
Calcula el valor total.
Busca productos.
Modifica stock y precios usando setters, con manejo de errores para entradas inválidas.
Compara productos con selección interactiva y búsqueda case-insensitive.

Manejo de errores: Usa try-except para capturar errores de validación y proporciona retroalimentación clara al usuario.
Interactividad: Un bucle de menú permite realizar múltiples acciones hasta que el usuario decide salir, mejorando la usabilidad.

Justificación del Diseño

Atributos privados (__stock,__productos): Protegen los datos críticos contra modificaciones no controladas, asegurando que el sistema mantenga un estado válido.
Atributo protegido (_precio): Permite flexibilidad para herencia futura mientras mantiene control mediante setters.
Getters/Setters: Centralizan las validaciones, asegurando que el stock y el precio cumplan con las restricciones en todo momento.
Abstracción: Simplifica la interacción al ocultar detalles internos, haciendo el sistema más intuitivo y mantenible.
Métodos especiales: Facilitan la integración con otras partes del código y mejoran la legibilidad.
Interfaz interactiva: Maximiza la usabilidad al permitir al usuario gestionar el inventario dinámicamente, respetando todas las restricciones del diseño.
