from gestor.gestor_tareas import GestorTareas
from extras.helpers import obtener_entrada_int, validar_prioridad, validar_fecha
from tareas.tarea_urgente import TareaUrgente
from tareas.tarea_recurrente import TareaRecurrente

def mostrar_menu():
    print("\n" + "="*50)
    print(" SISTEMA DE GESTIÓN DE TAREAS")
    print("="*50)
    print("1.  Agregar tarea normal")
    print("2.  Agregar tarea urgente")
    print("3.  Agregar tarea recurrente")
    print("4. Listar todas las tareas")
    print("5.  Listar solo tareas pendientes")
    print("6.  Marcar tarea como completada")
    print("7.  Eliminar tarea")
    print("8.  Buscar tareas")
    print("9.  Salir")
    print("-"*50)

def crear_tarea_normal(gestor):
    titulo = input(" Título: ").strip()
    if not titulo: 
        print(" Título vacío."); return
    descripcion = input(" Descripción: ").strip()
    prioridad = validar_prioridad(input(" Prioridad [media]: "))
    tarea = TareaRecurrente(titulo, descripcion, "única", prioridad)
    gestor.agregar_tarea(tarea)

def crear_tarea_urgente(gestor):
    titulo = input(" Título: ").strip()
    if not titulo: 
        print(" Título vacío."); return
    descripcion = input(" Descripción: ").strip()
    fecha = input(" Fecha límite (YYYY-MM-DD HH:MM): ").strip()
    if not validar_fecha(fecha):
        print(" Formato inválido."); return
    prioridad = validar_prioridad(input(" Prioridad [alta]: "), ["alta", "media"])
    tarea = TareaUrgente(titulo, descripcion, fecha, prioridad)
    gestor.agregar_tarea(tarea)

def crear_tarea_recurrente(gestor):
    titulo = input("🔄 Título: ").strip()
    if not titulo: 
        print(" Título vacío."); return
    descripcion = input(" Descripción: ").strip()
    frecuencias = ["diaria", "semanal", "mensual"]
    freq = input("🔁 Frecuencia [semanal]: ").strip().lower()
    frecuencia = freq if freq in frecuencias else "semanal"
    prioridad = validar_prioridad(input(" Prioridad [media]: "))
    tarea = TareaRecurrente(titulo, descripcion, frecuencia, prioridad)
    gestor.agregar_tarea(tarea)

def main():
    print(" Iniciando Sistema...")
    gestor = GestorTareas()
    
    while True:
        mostrar_menu()
        opcion = input("Opción (1-9): ").strip()
        
        if opcion == "1": crear_tarea_normal(gestor)
        elif opcion == "2": crear_tarea_urgente(gestor)
        elif opcion == "3": crear_tarea_recurrente(gestor)
        elif opcion == "4": gestor.listar_tareas()
        elif opcion == "5": gestor.listar_tareas(True)
        elif opcion == "6":
            gestor.listar_tareas(True)
            if gestor._tareas:
                gestor.marcar_completada(obtener_entrada_int("ID: "))
        elif opcion == "7":
            gestor.listar_tareas()
            if gestor._tareas and input(" ¿Eliminar? (s/N): ").lower() == 's':
                gestor.eliminar_tarea(obtener_entrada_int("ID: "))
        elif opcion == "8":
            texto = input(" Buscar: ").strip()
            if texto: gestor.buscar_tareas(texto)
        elif opcion == "9":
            print("👋 ¡Hasta luego!")
            break
        else: print(" Opción inválida.")
        
        input("\n Enter para continuar...")

if __name__ == "__main__":
    main()