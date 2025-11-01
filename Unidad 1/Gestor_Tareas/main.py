"""
Módulo que controla el flujo del programa de gestión de tareas.
"""

from Modulos.modelo import GestorTareas
from Modulos.utilidades import obtener_opcion_valida, formatear_tarea

def main():
    """
    Función que inicia el gestor de tareas y controla el menú.

    No recibe parámetros.
    No retorna valores.
    """
    gestor = GestorTareas()
    while True:
        print("\nGestor de Tareas")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        
        opcion = obtener_opcion_valida("Elige una opción (1-5): ", 1, 5)
        
        if opcion == 1:
            descripcion = input("Descripción de la tarea: ").strip()
            if descripcion:
                gestor.agregar_tarea(descripcion)
                print("Tarea agregada.")
            else:
                print("Descripción vacía. No se agregó la tarea.")
        
        elif opcion == 2:
            tareas = gestor.obtener_tareas()
            if not tareas:
                print("No hay tareas.")
            else:
                for idx, tarea in enumerate(tareas, 1):
                    print(formatear_tarea(idx, tarea))
        
        elif opcion == 3:
            tareas = gestor.obtener_tareas()
            if not tareas:
                print("No hay tareas para marcar.")
            else:
                idx = obtener_opcion_valida("Número de tarea a marcar: ", 1, len(tareas)) - 1
                gestor.marcar_completada(idx)
                print("Tarea marcada como completada.")
        
        elif opcion == 4:
            tareas = gestor.obtener_tareas()
            if not tareas:
                print("No hay tareas para eliminar.")
            else:
                idx = obtener_opcion_valida("Número de tarea a eliminar: ", 1, len(tareas)) - 1
                gestor.eliminar_tarea(idx)
                print("Tarea eliminada.")
        
        elif opcion == 5:
            print("Saliendo del programa.")
            break

if __name__ == "__main__":
    main()