import pytest
import calculator as calc

@pytest.mark.parametrize("val1, val2, expected", [
    (1, 2, 3),          #The same test case as test_add_ex1() in branch: exercise5
    (-1, 1, 0),         #Test to check for negative numbers
    (0.1, 0.2, 0.3)     #The same test case as test_add_ex2() in branch: exercise5
])

def test_add_ex1(val1: float, val2: float, expected: float)-> None:
    res = calc.add(val1, val2)
    assert res == pytest.approx(expected)

@pytest.mark.parametrize("val1, val2, expected", [
    (5, 7, 12),         #Positive numbers
    (-3, -4, -7),       #Negative numbers
    (1000, 0, 1000)     #Using 0
])
def test_add_ex2(val1: float, val2: float, expected: float) -> None:
    res = calc.add(val1, val2)
    assert res == pytest.approx(expected)
    #Testing type
    assert isinstance(res, (int, float))
    #Testing value
    assert res >= min(val1, val2) or res <= max(val1, val2)