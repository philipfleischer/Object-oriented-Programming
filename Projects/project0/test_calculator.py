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
   