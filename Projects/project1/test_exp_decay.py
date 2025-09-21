import numpy as np
import pytest
from exp_decay import ExponentialDecay

#Test right hand side = test_rhs
def test_rhs() -> None:
    """
    Testing right hand side (RHS) of the diff equation du/dt = -au
    Run with: pytest test_exp_decay.py"""
    #Right side does not contain t, so t can be variable
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
    a = -1.0
    with pytest.raises(ValueError):
        should_fail = ExponentialDecay(a)

def test_negative_decay_raises_ValueError() -> None:
    a = 0.4
    model = ExponentialDecay(a)
    with pytest.raises(ValueError):
        model.decay = -1.0

def test_num_states() -> None:
    a = 0.4
    model = ExponentialDecay(a)
    assert model.num_states == 1
    with pytest.raises(AttributeError):
        model.num_states = 2
    