"""Capacidad total y cupos ocupados. Devuelve cupos disponibles."""


def _es_entero(valor):
    # bool es subclase de int en Python, así que se excluye explícitamente
    return isinstance(valor, int) and not isinstance(valor, bool)


def calcular_cupos_disponibles(capacidad_total, cupos_ocupados):
    if not _es_entero(capacidad_total) or not _es_entero(cupos_ocupados):
        raise ValueError(
            "La capacidad total y los cupos ocupados deben ser números enteros."
        )

    if capacidad_total < 0 or cupos_ocupados < 0:
        raise ValueError("Los valores no pueden ser números negativos.")

    if cupos_ocupados > capacidad_total:
        raise ValueError(
            "los cupos ocupados sobrepasan la capacidad de cupos disponibles"
        )

    return capacidad_total - cupos_ocupados