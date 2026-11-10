import random
import pytest
from modules.grupo_04.logic import calcular_cupos_disponibles

def test_grupo_04_page(client):
    assert client.get("/modulos/grupo_04/").status_code == 200

def test_caso_valido_aleatorio():
    capacidad = random.randint(1, 1000)
    ocupados = random.randint(0, capacidad)
    
    resultado = calcular_cupos_disponibles(capacidad, ocupados)
    assert resultado == capacidad - ocupados
    assert resultado >= 0

def test_caso_limite_aleatorio():
    capacidad_y_ocupados = random.randint(1, 500)
    resultado = calcular_cupos_disponibles(capacidad_y_ocupados, capacidad_y_ocupados)
    assert resultado == 0

def test_caso_invalido_cupos_excedidos_aleatorio():
    capacidad = random.randint(1, 100)
    ocupados = capacidad + random.randint(1, 100)
    
    with pytest.raises(ValueError, match="los cupos ocupados sobrepasan la capacidad de cupos disponibles"):
        calcular_cupos_disponibles(capacidad, ocupados)

def test_valores_negativos_aleatorios():
    val_negativo = random.randint(-100, -1)
    val_positivo = random.randint(0, 100)
    
    with pytest.raises(ValueError, match="Los valores no pueden ser números negativos."):
        calcular_cupos_disponibles(val_negativo, val_positivo)
        
    with pytest.raises(ValueError, match="Los valores no pueden ser números negativos."):
        calcular_cupos_disponibles(val_positivo, val_negativo)

def test_tipos_invalidos():
    with pytest.raises(ValueError, match="La capacidad total y los cupos ocupados deben ser números enteros."):
        calcular_cupos_disponibles("100", 30)

    with pytest.raises(ValueError, match="La capacidad total y los cupos ocupados deben ser números enteros."):
        calcular_cupos_disponibles(100.5, 30)