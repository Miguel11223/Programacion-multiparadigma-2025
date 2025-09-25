

tasks = []

while True:
    print("\nMenu:")
    print("1. Agregar tarea")
    print("2. Listar tareas actuales")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    
    opcion = input("Elige una opcion: ")
    
    if opcion == '1':
        descripcion = input("Ingrese la nueva tarea: ")
        tasks.append({'descripcion': descripcion, 'completada': False})
        print("Tarea agregada.")
    
    elif opcion == '2':
        pending = [t for t in tasks if not t['completada']]
        if not pending:
            print("No hay tareas pendientes.")
        else:
            print("Tareas pendientes:")
            for i, t in enumerate(pending, 1):
                print(f"{i}. {t['descripcion']}")
    
    elif opcion == '3':
        pending = [t for t in tasks if not t['completada']]
        if not pending:
            print("No hay tareas pendientes.")
            continue
        print("Tareas pendientes:")
        for i, t in enumerate(pending, 1):
            print(f"{i}. {t['descripcion']}")
        try:
            num = int(input("Ingrese el número de la tarea a marcar como completada: ")) - 1
            if 0 <= num < len(pending):
                pending[num]['completada'] = True
                print("Tarea marcada como completada.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida. Debe ser un número.")
    
    elif opcion == '4':
        pending = [t for t in tasks if not t['completada']]
        if not pending:
            print("No hay tareas pendientes.")
            continue
        print("Tareas pendientes:")
        for i, t in enumerate(pending, 1):
            print(f"{i}. {t['descripcion']}")
        try:
            num = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
            if 0 <= num < len(pending):
                tasks.remove(pending[num])
                print("Tarea eliminada.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida. Debe ser un número.")
    
    elif opcion == '5':
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción inválida. Intente de nuevo.")