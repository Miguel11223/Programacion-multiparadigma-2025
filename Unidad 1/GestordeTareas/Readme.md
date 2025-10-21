# **Sistema de Gestión de Tareas**

Permite crear, organizar y gestionar tareas diarias con diferentes prioridades y tipos y guarda automáticamente las tareas en JSON.

## **¿Qué Hace?**

1. **CREAR** tareas normales, urgentes o recurrentes
2. **LISTAR** todas o solo pendientes (ordenadas por prioridad)
3. **COMPLETAR** tareas marcándolas como hechas
4. **ELIMINAR** tareas que ya no necesitas
5. **BUSCAR** tareas por nombre o descripción
6. **GUARDAR** todo automáticamente en `tareas.json`

## **Tipos de Tareas**

| **Tipo** | **Para qué sirve** | **Ejemplo** |
|----------|-------------------|-------------|
| **Normal** | Tareas simples | "Comprar pan" |
| **Urgente** | Con fecha límite | "Entregar informe [hoy 17:00]" |
| **Recurrente** | Se repiten | "Hacer ejercicio [diaria]" |

## **Estructura**

gestor_tareas/
├── tareas/     # Define QUÉ es una tarea
├── gestor/     # MANEJA la lista de tareas
├── extras/      # GUARDA y carga desde JSON
└── main.py     # MENÚ para usar el sistema.
