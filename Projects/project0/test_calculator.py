# To run test:
# Run command in terminal: pytest
# With Verbose: pytest -v
# You might want to run in conda environment:
# pip install pytest

import pytest
import math
import calculator as calc

@pytest.mark.parametrize("val1, val2, expected", [
    (1, 2, 3),          #Simple test case
    (-1, 1, 0),         #Test case for negative numbers
    (0.1, 0.2, 0.3)     #Test case for float values, use approx
])

def test_add(val1: float, val2: float, expected: float) -> None:
    res = calc.add(val1, val2)
    assert res == pytest.approx(expected)

@pytest.mark.parametrize("val1, val2, expected", [
    (10, 5, 2),
    (10, -5, -2),
    (10, 1, 10)
])
def test_divide(val1: float, val2: float, expected: float) -> None:
    res = calc.divide(val1, val2)
    assert res == pytest.approx(expected)

@pytest.mark.parametrize("val, expected", [
    (9, 362880),
    (2, 2),
    (19, 121645100408832000)
])
def test_factorial(val: int, expected: int) -> None:
    res = calc.factorial(val)
    assert res == expected

@pytest.mark.parametrize("val, expected", [
    (0, 0),
    (math.pi/4, math.sqrt(2)/2),
    (math.pi/2, 1),
    (3*math.pi/2, -1)
])
def test_sin(val: float, expected: float) -> None:
    assert calc.sin(val) == pytest.approx(expected, rel=1e-6)

@pytest.mark.parametrize("inp, exp_exc", [
    (-1, ValueError),       #Negative value to get ValueError
    (1.5, TypeError),       #Decimal value to get TypeError
    ("Hallo", TypeError)    #Non-integer value to get TypeError
])
def test_factorial_exceptions(inp: int, exp_exc: int) -> None:
    with pytest.raises(exp_exc):
        calc.factorial(inp)


def test_divide_by_zero() -> None:
    """We do not need this manually, since Python already
    checks for this scenario"""
    with pytest.raises(ZeroDivisionError):
        calc.divide(2, 0)