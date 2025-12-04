#Parte 2

#1.Filtrar ventas mayores a 100
def es_venta_mayor_a_cien(venta):
    return venta['monto'] > 100

#2. Aplicar 15% de impuesto
def aplicar_impuesto_y_formatear(venta):
    monto_original = venta['monto']
    monto_con_impuesto = monto_original * 1.15

    return {
        'id': venta['id'],
        'monto_original': monto_original,
        'monto_final': monto_con_impuesto
    }

def procesar_ventas_funcional(ventas):
    ventas_filtradas = filter(es_venta_mayor_a_cien, ventas)
    
    ventas_procesadas = list(map(aplicar_impuesto_y_formatear, ventas_filtradas))
    
    total = sum(v['monto_final'] for v in ventas_procesadas)
    
    return ventas_procesadas, total


ventas_ejemplo = [ 
    {'id': 1, 'monto': 50},
    {'id': 2, 'monto': 150},
    {'id': 3, 'monto': 200},
    {'id': 4, 'monto': 80},
    {'id': 5, 'monto': 300},
]

resultados_funcional, total_funcional = procesar_ventas_funcional(ventas_ejemplo)

print("Resultados")
print("Ventas Procesadas:")
for v in resultados_funcional:
    print(v)
print(f"\nTotal: {total_funcional:.2f}")