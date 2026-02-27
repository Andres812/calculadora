import pytest
from calculator import *

def test_suma():
    assert suma(2,3) == 5

def test_resta():
    assert resta(5,2) == 3

def test_multiplicacion():
    assert multiplicacion(3,4) == 12

def test_division():
    assert division(10,2) == 5

def test_division_cero():
    import pytest
    with pytest.raises(ValueError):
        division(5,0)