from calculator import add

def test_add():
    res = add(1, 2)
    assert res == 3, f"Expected the sum to be 3, not {res}" 
    

test_add()
