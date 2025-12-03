#Parte 1

# Función B
contador = 0
def siguiente_id():
    global contador
    contador += 1
    return f"ID-{contador}"


#Funcion B correccion pura
def siguiente_id_pura(contador_actual):
    nuevo_contador = contador_actual + 1
    nuevo_id = f"ID-{nuevo_contador}"
    return nuevo_id, nuevo_contador  

# Función C
def agregar_fecha(registro):
    from datetime import datetime
    registro['fecha'] = datetime.now().isoformat()
    return registro

#Funcion C correccion pura
def agregar_fecha_pura(registro, fecha_actual):
    registro_copia = registro.copy()
    registro_copia['fecha'] = fecha_actual
    return registro_copia


# Función E
import random
def mezclar_lista(lista):
    random.shuffle(lista)
    return lista

#Funcion E correccion pura
import random
def mezclar_lista_pura(lista):
    lista_copia = list(lista)
    random.shuffle(lista_copia) 
    return lista_copia


