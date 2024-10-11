import pytest
from calculator import Calculator


def test_addition():
    """Test add()"""
    calc = Calculator()
    assert calc.add(5) == 5
    assert calc.add(3) == 8


def test_subtraction():
    """Test subtract()"""
    calc = Calculator()
    calc.add(10)
    assert calc.subtract(3) == 7


def test_multiplication():
    """Test multiply()"""
    calc = Calculator()
    calc.add(2)
    assert calc.multiply(3) == 6


def test_division():
    """Test divide()"""
    calc = Calculator()
    calc.add(10)
    assert calc.divide(2) == 5
    with pytest.raises(ValueError):
        calc.divide(0)


def test_root():
    """Test root()"""
    calc = Calculator()
    calc.add(16)
    assert calc.root(2) == 4
    with pytest.raises(ValueError):
        calc.add(-32)
        calc.root(2)


def test_reset():
    """Test reset()"""
    calc = Calculator()
    calc.add(5)
    calc.reset()
    assert calc.memory == 0.0
