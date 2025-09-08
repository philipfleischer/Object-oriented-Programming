import numpy as np
from exp_decay import ExponentialDecay

#Test right hand side = test_rhs
def test_rhs() -> None:
    """Tester hørye side (RHS) av difflikningen du/dt = -au
    Kjøres med: pytest test_exp_decay.py"""
    
    #Hørye side inneholder ikke t, så t kan være hva som helst
    t = 0.0

    model = ExponentialDecay(0.4)       #a = 0.4
    u = np.array([3.2])                 #u = 3.2

    du_dt = model(t, u)
    #Using np.isclose on float numbers, to get approx values
    assert np.isclose(du_dt == -1.28)   # u'(t) = -1.28