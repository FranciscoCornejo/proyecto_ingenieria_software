from math import isfinite

def kilometers_to_meters(value):
    try:
        number = float(value)
    except (ValueError, TypeError):
        raise ValueError("Ingresa un número válido.") from None
    if not isfinite(number) or not 0 <= number <= 1_000_000:
        raise ValueError("Ingresa kilómetros entre 0 y 1.000.000.")
    return number * 1000
