from calculator import add
from pytest import approx

def test_add_ex1():
    res = add(1, 2)
    assert res == 3, f"Expected the sum to be 3, not {res}" 
    


def test_add_ex2():
    val1 = 0.1
    val2 = 0.2
    res = add(val1, val2)
    assert res == approx(0.3), f"Expected the sum to be 0.3, not {res}" 
    
