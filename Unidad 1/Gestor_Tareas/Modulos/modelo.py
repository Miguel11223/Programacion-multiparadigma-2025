"""
Módulo que contiene la clase principal para modelar y gestionar tareas.
Define la estructura de datos y operaciones básicas sobre las tareas.
"""

class GestorTareas:
    """
    Clase que gestiona una lista de tareas.

    Atributos:
        tareas (list): Lista de diccionarios, cada uno representando una tarea
                       con claves 'descripcion' (str) y 'completada' (bool).
    """

    def __init__(self):
        """
        Inicializa el gestor con una lista vacía de tareas.

        No recibe parámetros.
        No retorna valores.
        """
        self.tareas = []

    def agregar_tarea(self, descripcion):
        """
        Agrega una nueva tarea a la lista.

        Parámetros:
            descripcion (str): Texto descriptivo de la tarea.

        No retorna valores.
        """
        self.tareas.append({"descripcion": descripcion, "completada": False})

    def obtener_tareas(self):
        """
        Retorna la lista completa de tareas.

        No recibe parámetros.

        Retorna:
            list: Lista de diccionarios de tareas.
        """
        return self.tareas

    def marcar_completada(self, indice):
        """
        Marca una tarea específica como completada.

        Parámetros:
            indice (int): Índice de la tarea en la lista (0-based).

        No retorna valores. Ignora si el índice es inválido.
        """
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]["completada"] = True

    def eliminar_tarea(self, indice):
        """
        Elimina una tarea específica de la lista.

        Parámetros:
            indice (int): Índice de la tarea en la lista (0-based).

        No retorna valores. Ignora si el índice es inválido.
        """
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]