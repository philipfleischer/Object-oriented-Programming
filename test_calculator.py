from calculator import add
import pytest

@pytest.mark.parametrize("val1, val2, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0.1, 0.2, 0.3)
])
def test_add(val1, val2, expected):
    res = add(val1, val2)
    assert res == pytest.approx(expected)
    
