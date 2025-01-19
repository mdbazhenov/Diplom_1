import pytest
from praktikum.bun import Bun

def test_constructor_initialization():
    bun = Bun("Булка", 1.5)
    assert bun.name == "Булка"
    assert bun.price == 1.5

def test_get_name():
    bun = Bun("Хлеб", 2.0)
    assert bun.get_name() == "Хлеб"

def test_get_price():
    bun = Bun("Фокачо", 3.0)
    assert bun.get_price() == 3.0



