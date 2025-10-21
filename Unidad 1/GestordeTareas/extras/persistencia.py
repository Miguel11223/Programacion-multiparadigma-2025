import json
import os
from typing import List
from tareas.tarea import Tarea
from tareas.tarea_urgente import TareaUrgente
from tareas.tarea_recurrente import TareaRecurrente

class PersistenciaTareas:
    def __init__(self, archivo: str):
        self._archivo = archivo
    
    def guardar(self, tareas: List[Tarea]):
        try:
            datos = [tarea.to_dict() for tarea in tareas]
            with open(self._archivo, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f" Error al guardar: {e}")
    
    def cargar(self) -> List[Tarea]:
        if not os.path.exists(self._archivo):
            return []
        
        try:
            with open(self._archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            
            tareas = []
            for data in datos:
                try:
                    if data['tipo'] == 'TareaUrgente':
                        tarea = TareaUrgente.from_dict(data)
                    elif data['tipo'] == 'TareaRecurrente':
                        tarea = TareaRecurrente.from_dict(data)
                    else:
                        continue
                    tareas.append(tarea)
                except KeyError:
                    continue
            return tareas
        except Exception as e:
            print(f" Error al cargar: {e}")
            return []