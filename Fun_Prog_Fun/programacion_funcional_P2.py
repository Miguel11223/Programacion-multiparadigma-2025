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
