from .tarea import Tarea
from typing import Dict, Any
from datetime import datetime

class TareaUrgente(Tarea):
    def __init__(self, titulo: str, descripcion: str, fecha_limite: str, prioridad: str = "alta"):
        super().__init__(titulo, descripcion, prioridad)
        self._fecha_limite = fecha_limite
    
    @property
    def fecha_limite(self) -> str: return self._fecha_limite
    
    def mostrar_info(self) -> str:
        estado = " COMPLETADA" if self._completada else "⏳ PENDIENTE"
        return f" [URGENTE] {self._titulo} | {estado}\n   Descripción: {self._descripcion}\n   Prioridad: {self._prioridad.upper()}\n   Fecha límite: {self._fecha_limite}\n   Creada: {self._fecha_creacion}"
    
    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data['fecha_limite'] = self._fecha_limite
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TareaUrgente':
        tarea = cls(data['titulo'], data['descripcion'], data['fecha_limite'], data['prioridad'])
        tarea.id = data['id']
        tarea.completada = data['completada']
        tarea._fecha_creacion = data['fecha_creacion']
        return tarea