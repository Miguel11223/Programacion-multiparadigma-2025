from .tarea import Tarea
from typing import Dict, Any

class TareaRecurrente(Tarea):
    def __init__(self, titulo: str, descripcion: str, frecuencia: str, prioridad: str = "media"):
        super().__init__(titulo, descripcion, prioridad)
        self._frecuencia = frecuencia
    
    @property
    def frecuencia(self) -> str: return self._frecuencia
    
    def mostrar_info(self) -> str:
        estado = "✅ COMPLETADA" if self._completada else " PENDIENTE"
        freq_display = "ÚNICA" if self._frecuencia == "única" else self._frecuencia.upper()
        return f"🔄 [{freq_display}] {self._titulo} | {estado}\n   Descripción: {self._descripcion}\n   Prioridad: {self._prioridad.upper()}\n   Frecuencia: {freq_display}\n   Creada: {self._fecha_creacion}"
    
    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data['frecuencia'] = self._frecuencia
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TareaRecurrente':
        tarea = cls(data['titulo'], data['descripcion'], data['frecuencia'], data['prioridad'])
        tarea.id = data['id']
        tarea.completada = data['completada']
        tarea._fecha_creacion = data['fecha_creacion']
        return tarea