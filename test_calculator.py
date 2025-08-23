from calculator import add
import math

def test_add_ex1():
    res = add(1, 2)
    assert res == 3, f"Expected the sum to be 3, not {res}" 
    


def test_add_ex2():
    val1 = 0.1
    val2 = 0.2
    res = abs(add(val1, val2))
    assert abs(res) == 0.3, f"Expected the sum to be 0.3, not {res}" 
    
