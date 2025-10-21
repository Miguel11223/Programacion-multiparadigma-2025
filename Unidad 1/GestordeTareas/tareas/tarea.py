from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, Any

class Tarea(ABC):
    def __init__(self, titulo: str, descripcion: str, prioridad: str = "media"):
        self._id = None
        self._titulo = titulo
        self._descripcion = descripcion
        self._prioridad = prioridad
        self._completada = False
        self._fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @property
    def id(self) -> int: return self._id
    @id.setter
    def id(self, value: int): self._id = value
    
    @property
    def titulo(self) -> str: return self._titulo
    @property
    def descripcion(self) -> str: return self._descripcion
    @property
    def prioridad(self) -> str: return self._prioridad
    @property
    def completada(self) -> bool: return self._completada
    @completada.setter
    def completada(self, value: bool): self._completada = value
    @property
    def fecha_creacion(self) -> str: return self._fecha_creacion
    
    @abstractmethod
    def mostrar_info(self) -> str: pass
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self._id, 'titulo': self._titulo, 'descripcion': self._descripcion,
            'prioridad': self._prioridad, 'completada': self._completada,
            'fecha_creacion': self._fecha_creacion, 'tipo': self.__class__.__name__
        }
    
    @classmethod
    @abstractmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Tarea': pass