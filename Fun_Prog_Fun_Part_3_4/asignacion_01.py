from functools import reduce

def crear_transformador(funcion):
    def transformador(lista):
        return list(map(funcion, lista))
    return transformador


def crear_filtro(predicado):
    def filtro(lista):
        return list(filter(predicado, lista))
    return filtro

def crear_reductor(funcion, valor_inicial):
    def reductor(lista):
       return reduce(funcion, lista, valor_inicial)
    return reductor

def componer(*funciones):
    def procesador_compuesto(dato):
        resultado = dato
        for func in funciones:
            resultado = func(resultado)
        return resultado
    return procesador_compuesto

numeros = [1, -2, 3, -4, 5, -6, 7, 8, -9, 10]

pipeline = componer(
    crear_filtro(lambda x: x > 0),             
    crear_transformador(lambda x: x ** 2),    
    crear_reductor(lambda acc, x: acc + x, 0)  
)

resultado = pipeline(numeros)
print(f"Resultado esperado: 248") 
print(f"Resultado: {resultado}")
