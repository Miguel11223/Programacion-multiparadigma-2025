"""
Módulo de utilidades con funciones auxiliares para validación y formateo.
Proporciona soporte para entradas de usuario y presentación de datos.
"""

def obtener_opcion_valida(mensaje, min_valor, max_valor):
    """
    Solicita al usuario un número entero válido dentro de un rango.

    Parámetros:
        mensaje (str): Texto a mostrar para solicitar la entrada.
        min_valor (int): Valor mínimo aceptable (inclusive).
        max_valor (int): Valor máximo aceptable (inclusive).

    Retorna:
        int: El número válido ingresado por el usuario.
    """
    while True:
        try:
            opcion = int(input(mensaje).strip())
            if min_valor <= opcion <= max_valor:
                return opcion
            print(f"Opción inválida. Debe estar entre {min_valor} y {max_valor}.")
        except ValueError:
            print("Entrada no válida. Ingresa un número entero.")

def formatear_tarea(indice, tarea):
    """
    Formatea una tarea para visualizarlo en texto.

    Parámetros:
        indice (int): Número de tarea para mostrar (1-based).
        tarea (dict): Diccionario con 'descripcion' y 'completada'.

    Retorna:
        str: Cadena formateada, e.g., "1. Tarea desc [Completada]".
    """
    estado = "[Completada]" if tarea["completada"] else "[Pendiente]"
    return f"{indice}. {tarea['descripcion']} {estado}"