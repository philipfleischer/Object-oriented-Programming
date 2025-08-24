from calculator import *
import pytest

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
    (9, 3265920),
    (-2, -2),
    (19, 2311256907767808000)
])
def test_factorial(val, expected):
    res = factorial(val)
    assert res == expected

@pytest.mark.parametrize("val, N, expected", [
    (10, 20, 100),
    (-1, 20, 100),
    (7, 20, -100)
])
def test_sin(val, N, expected):
    res = sin(val, N)
    assert res == pytest.approx(expected)
