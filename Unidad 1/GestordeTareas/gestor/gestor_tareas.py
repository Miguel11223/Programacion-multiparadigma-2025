from typing import List
from tareas.tarea import Tarea
from extras.persistencia import PersistenciaTareas

class GestorTareas:
    def __init__(self, archivo: str = "tareas.json"):
        self._tareas: List[Tarea] = []
        self._persistencia = PersistenciaTareas(archivo)
        self._proximo_id = 1
        self._cargar_tareas()
    
    def agregar_tarea(self, tarea: Tarea):
        tarea.id = self._proximo_id
        self._tareas.append(tarea)
        self._proximo_id += 1
        self._persistencia.guardar(self._tareas)
        print(f"✅ Tarea '{tarea.titulo}' agregada con ID: {tarea.id}")
    
    def listar_tareas(self, filtrar_completadas: bool = False):
        if not self._tareas:
            print("📭 No hay tareas registradas.")
            return
        
        tareas_filtradas = [t for t in self._tareas if not filtrar_completadas or not t.completada]
        if not tareas_filtradas:
            print(" No hay tareas pendientes.")
            return
        
        print(f"\n {'='*60}")
        print(f"{'Tareas' if not filtrar_completadas else 'Tareas Pendientes'} ({len(tareas_filtradas)})")
        print(f"{'='*60}")
        
        prioridades = {"alta": 3, "media": 2, "baja": 1}
        for tarea in sorted(tareas_filtradas, key=lambda t: prioridades.get(t.prioridad, 0), reverse=True):
            print(tarea.mostrar_info())
            print("-" * 60)
    
    def marcar_completada(self, tarea_id: int) -> bool:
        for tarea in self._tareas:
            if tarea.id == tarea_id:
                tarea.completada = True
                self._persistencia.guardar(self._tareas)
                print(f"✅ Tarea '{tarea.titulo}' marcada como completada.")
                return True
        print(f" No se encontró la tarea con ID: {tarea_id}")
        return False
    
    def eliminar_tarea(self, tarea_id: int) -> bool:
        for i, tarea in enumerate(self._tareas):
            if tarea.id == tarea_id:
                self._tareas.pop(i)
                self._persistencia.guardar(self._tareas)
                print(f"🗑️ Tarea '{tarea.titulo}' eliminada.")
                return True
        print(f" No se encontró la tarea con ID: {tarea_id}")
        return False
    
    def buscar_tareas(self, texto: str):
        resultados = [t for t in self._tareas if texto.lower() in t.titulo.lower() or texto.lower() in t.descripcion.lower()]
        if not resultados:
            print(f" No se encontraron tareas con '{texto}'")
            return
        
        print(f"\n Resultados para '{texto}' ({len(resultados)})")
        print(f"{'='*60}")
        for tarea in resultados:
            print(tarea.mostrar_info())
            print("-" * 60)
    
    def _cargar_tareas(self):
        self._tareas = self._persistencia.cargar()
        if self._tareas:
            self._proximo_id = max(t.id for t in self._tareas) + 1