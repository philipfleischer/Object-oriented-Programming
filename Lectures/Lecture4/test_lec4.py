import numpy as np
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

def test_vektor_addisjon_med_ulik_lengde():
    """Kjøres fra terminal: pytest test_lec4.py"""
    # TODO: Husk å teste hva som skjer hvis motsatt rekkefølge:
    #       vektor_addisjon(v, u)
    u = [1,2]
    v = [3,4,5,6]
    w = vektor_addisjon(u,v)

    korteste = min(len(u), len(v))
    lengste = max(len(u), len(v))

    assert len(w) == lengste

    for i in range(korteste, lengste):
        assert w[i] == v[i]
    
    u2 = [1,2,0,0]
    w2 = vektor_addisjon(u2, v)
    assert w == w2

def test_vektor_addisjon_med_desimaltall() -> None:
    """Kjøres fra terminal: pytest test_lec4.py"""
    u = [0.2, 0.5]
    v = [0.1, 0.5]
    w = vektor_addisjon(u,v)

    assert len(w) == len(u)
    assert len(w) == len(v)

    for i in range(len(w)):
        assert np.isclose(w[i] - u[i], v[i])
        assert np.isclose(w[i] - v[i], u[i])

    assert np.isclose(sum(w), sum(u) + sum(v))