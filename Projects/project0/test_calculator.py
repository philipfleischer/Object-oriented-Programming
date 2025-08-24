import pytest
import math
from calculator import *

@pytest.mark.parametrize("val1, val2, expected", [
    (1, 2, 3),          #The same test case as test_add_ex1() in branch: exercise5
    (-1, 1, 0),         #Test to check for negative numbers
    (0.1, 0.2, 0.3)     #The same test case as test_add_ex2() in branch: exercise5
])

def test_add(val1, val2, expected):
    res = add(val1, val2)
    assert res == pytest.approx(expected)
   
@pytest.mark.parametrize("val1, val2, expected", [
    (10, 5, 2),
    (10, -5, -2),
    (10, 1, 10)
])
def test_divide(val1, val2, expected):
    res = divide(val1, val2)
    assert res == pytest.approx(expected)

@pytest.mark.parametrize("val, expected", [
    (9, 362880),
    (2, 2),
    (19, 121645100408832000)
])
def test_factorial(val, expected):
    res = factorial(val)
    assert res == expected

@pytest.mark.parametrize("val, expected", [
    (0, 0),
    (math.pi/4, math.sqrt(2)/2),
    (math.pi/2, 1),
    (3*math.pi/2, -1)
])
def test_sin(val, expected):
    assert sin(val, N=20) == pytest.approx(expected, rel=1e-6)
