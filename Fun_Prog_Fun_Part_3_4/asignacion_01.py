from functools import reduce

def crear_transformador(funcion):
    def transformador(lista):
        return list(map(funcion, lista))
    return transformador


def crear_filtro(predicado):
    def filtro(lista):
        return list(filter(predicado, lista))
    return filtro

