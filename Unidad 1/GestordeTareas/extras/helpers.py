from datetime import datetime

def obtener_entrada_int(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print(" Por favor, ingrese un número válido.")

def validar_prioridad(prioridad: str, opciones: list = None) -> str:
    if opciones is None:
        opciones = ["baja", "media", "alta"]
    prioridad = prioridad.strip().lower()
    return prioridad if prioridad in opciones else opciones[1]

def validar_fecha(fecha: str, formato: str = "%Y-%m-%d %H:%M") -> bool:
    try:
        datetime.strptime(fecha, formato)
        return True
    except ValueError:
        return False