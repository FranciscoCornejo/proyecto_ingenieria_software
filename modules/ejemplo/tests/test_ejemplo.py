import pytest
from modules.ejemplo.logic import kilometers_to_meters

@pytest.mark.parametrize("value,expected", [("2", 2000), ("0", 0), ("1.5", 1500)])
def test_conversion(value, expected):
    assert kilometers_to_meters(value) == expected

@pytest.mark.parametrize("value", ["", "abc", "-1", "nan", "inf", "1000001"])
def test_invalid(value):
    with pytest.raises(ValueError):
        kilometers_to_meters(value)

def test_result_in_page(client):
    response = client.get("/modulos/ejemplo/?km=2")
    assert response.status_code == 200
    assert b"2000.0 metros" in response.data

def test_invalid_page(client):
    response = client.get("/modulos/ejemplo/?km=abc")
    assert response.status_code == 400
    assert 'número válido'.encode() in response.data
