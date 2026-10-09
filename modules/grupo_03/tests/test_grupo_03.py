def test_grupo_03_page(client):
    assert client.get("/modulos/grupo_03/").status_code == 200

# Agregar pruebas del cálculo y de entradas inválidas cuando implementen la función.
