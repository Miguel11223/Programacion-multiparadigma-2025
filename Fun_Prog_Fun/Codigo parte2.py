def procesar_ventas(ventas):
    """
    CODIGO IMPERATIVO: 
    1. Filtrar ventas mayores a $100
    2. Aplicar 15% de impuesto
    3. Calcular el total
    """
    
    resultado = [] 
    total = 0

    for venta in ventas:
        if venta['monto'] > 100:
            monto_con_impuesto = venta['monto'] * 1.15
            
            nueva_venta = {
                'id': venta['id'],
                'monto_original': venta['monto'],
                'monto_final': monto_con_impuesto 
            }
            
            resultado.append(nueva_venta)
            total += monto_con_impuesto 

    return resultado, total

ventas_ejemplo = [ 
    {'id': 1, 'monto': 50},
    {'id': 2, 'monto': 150},
    {'id': 3, 'monto': 200},
    {'id': 4, 'monto': 80},
    {'id': 5, 'monto': 300},
]

resultados_imperativo, total_imperativo = procesar_ventas(ventas_ejemplo)

print("Resultados")
print("Ventas Procesadas:")
for v in resultados_imperativo:
    print(v)
print(f"\nTotal Calculado: ${total_imperativo:.2f}")