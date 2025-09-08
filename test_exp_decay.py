import numpy as np
import pytest
from exp_decay import ExponentialDecay

#Test right hand side = test_rhs
def test_rhs() -> None:
    """
    Tester hørye side (RHS) av difflikningen du/dt = -au
    Kjøres med: pytest test_exp_decay.py"""
    #Hørye side inneholder ikke t, så t kan være hva som helst
    t = 0.0

    # pointing to new ExponentialDecay object
    model = ExponentialDecay(0.4)       #a = 0.4
    u = np.array([3.2])                 #u = 3.2

    """using model as a function. Trying to do two 
     things simulataneously. We make an object model and use it as
     a function (callable, to function like a function in the 
     callable call, but an object in every other instance.) """
    du_dt = model(t, u)
    #Using np.isclose on float numbers, to get approx values
    assert np.isclose(du_dt, -1.28)   # u'(t) = -1.28

def test_negative_decay_raises_ValueError_constructor() -> None:
    """Tester at a ikke kan være negativ
    Kjøres med: pytest test_exp_decay.py"""

    a = -1.0
    with pytest.raises(ValueError):
        should_fail = ExponentialDecay(a)

def test_negative_decay_raises_ValueError() -> None:
    """Tester at a ikke kan endres til å være negativ
    Kjøres med: pytest test_exp_decay.py"""
    a = 0.4
    model = ExponentialDecay(a)
    with pytest.raises(ValueError):
        model.decay = -1.0