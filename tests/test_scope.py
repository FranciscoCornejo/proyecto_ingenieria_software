import pytest
from scripts.check_scope import violations

def test_scope():
    assert not violations("grupo_01", ["modules/grupo_01/service.py"])
    assert violations("grupo_01", ["app/__init__.py", "modules/grupo_02/README.md"])
    assert violations("grupo_01", ["modules/grupo_010/x.py"])
    with pytest.raises(ValueError):
        violations("main", [])
