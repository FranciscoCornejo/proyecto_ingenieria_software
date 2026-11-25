def test_grupo_09_page(client):
    assert client.get("/modulos/grupo_09/").status_code == 200

import pytest
from modules.grupo_09.logic import calcular_cotizacion

def test_cotizacion_valida():
    res = calcular_cotizacion(20, 1000)
    assert res["porcentaje_descuento"] == 10
    assert res["total_a_pagar"] == 18000.0

def test_cotizacion_limite():
    res = calcular_cotizacion(10, 500)
    assert res["porcentaje_descuento"] == 10
    assert res["total_a_pagar"] == 4500.0

def test_cotizacion_invalida():
    with pytest.raises(ValueError):
        calcular_cotizacion(0, 1000)
