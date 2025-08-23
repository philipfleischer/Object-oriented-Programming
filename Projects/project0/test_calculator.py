from calculator import add

def test_add_ex1():
    res = add(1, 2)
    assert res == 3, f"Expected the sum to be 3, not {res}" 
    
test_add_ex1()

def test_add_ex2():
    res = add(0.1, 0.2)
    assert res == 0.3, f"Expected the sum to be 3, not {res}" 
    
test_add_ex2()