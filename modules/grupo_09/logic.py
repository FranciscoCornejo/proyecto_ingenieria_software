def calcular_cotizacion(cantidad, precio_unitario):
    """
    Calcula el subtotal, el porcentaje de descuento según el tramo,
    el monto del descuento y el total a pagar.
    """
    # Validaciones básicas
    if not isinstance(cantidad, int) or cantidad <= 0:
        raise ValueError("La cantidad debe ser un entero mayor a 0.")
    if not isinstance(precio_unitario, (int, float)) or precio_unitario < 0:
        raise ValueError("El precio unitario debe ser un número mayor o igual a 0.")

    # Reglas de descuento automatizado por cantidad
    if 1 <= cantidad <= 9:
        porcentaje_descuento = 0
    elif 10 <= cantidad <= 49:
        porcentaje_descuento = 10
    elif 50 <= cantidad <= 99:
        porcentaje_descuento = 15
    else:  # 100 o más
        porcentaje_descuento = 20

    # Fórmulas de cálculo
    subtotal = cantidad * precio_unitario
    monto_descuento = subtotal * (porcentaje_descuento / 100)
    total_a_pagar = subtotal - monto_descuento

    # Redondeo estándar a 2 decimales
    return {
        "subtotal": round(subtotal, 2),
        "porcentaje_descuento": porcentaje_descuento,
        "monto_descuento": round(monto_descuento, 2),
        "total_a_pagar": round(total_a_pagar, 2)
    }