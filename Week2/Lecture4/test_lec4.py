from lec4 import vektor_addisjon

def test_vektor_addisjon_med_heltall() -> None:
    """Kjøres fra terminal: pytest test_lec4.py"""
    u = [2,3,4]
    v = [-1,0,1]
    w = vektor_addisjon(u,v)

    assert len(w) == len(u)
    assert len(w) == len(v)

    for i in range(len(w)):
        assert w[i] - u[i] == v[i]
        assert w[i] - v[i] == u[i]

    assert sum(w) == sum(u) + sum(v)

    