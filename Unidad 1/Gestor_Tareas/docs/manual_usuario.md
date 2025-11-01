# Manual de Usuario: Gestor de Tareas

## Propósito del Programa

El propósito de este programa es proporcionar una herramienta simple y modular en Python para la gestión de tareas personales. Permite a los usuarios agregar nuevas tareas, listarlas con su estado (pendiente o completada), marcar tareas como terminadas y eliminarlas.

## Introducción

Este es un programa simple en Python para gestionar tareas. Permite agregar, listar, marcar como completadas y eliminar tareas a través de un menú interactivo.

## Cómo Ejecutar el Proyecto

1. Abre la carpeta `gestor_tareas/` en tu terminal o línea de comandos.
2. Ejecuta el comando: `python main.py`.
3. El programa se iniciará mostrando un menú interactivo.
4. Para detener el programa, selecciona la opción "5. Salir" en el menú.

## Módulos Contenidos y su Función

- **main.py**: Este es el archivo principal que controla el flujo general del programa. Importa los otros módulos, crea una instancia de la clase principal y presenta un menú interactivo al usuario para manejar las operaciones de tareas.

- **modulos/modelo.py**: Contiene la clase principal `GestorTareas`, que modela la lógica central del sistema. Maneja el almacenamiento y manipulación de las tareas (como agregar, obtener, marcar como completadas y eliminar).

- **modulos/utilidades.py**: Incluye funciones auxiliares de apoyo, como validación de entradas de usuario y formateo de salida. Estas funciones son reutilizables y separan la lógica secundaria del núcleo del programa.

- **modulos/**init**.py**: Archivo vacío que convierte la carpeta `modulos` en un paquete Python, permitiendo importaciones relativas o absolutas desde otros archivos.

Todos los módulos incluyen docstrings detallados que explican su propósito, funciones, parámetros y valores de retorno, facilitando la comprensión y mantenimiento del código.

## Opciones del Menú

- **1. Agregar tarea**: Ingresa una descripción y presiona Enter.
- **2. Listar tareas**: Muestra todas las tareas con su estado (Pendiente o Completada).
- **3. Marcar tarea como completada**: Ingresa el número de la tarea a marcar.
- **4. Eliminar tarea**: Ingresa el número de la tarea a eliminar.
- **5. Salir**: Termina el programa.
