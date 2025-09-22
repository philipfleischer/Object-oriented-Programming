import numpy as np
import pytest
from exp_decay import ExponentialDecay
from ode import InvalidInitialConditionError

#Cases for testing: (a, u0_scalar, T, dt)
TEST_CASES = [
    (0.4, 3.2, 10.0, 0.01),
    (1.0, 2.0, 2.0, 0.05),
    (0.2, 1.5, 5.0, 0.10)
]

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
    
def test_solve_with_different_number_of_initial_states() -> None:
    a = 0.4
    model = ExponentialDecay(a)
    u0_wrong = np.array([1.0, 2.0])

    with pytest.raises(InvalidInitialConditionError):
        model.solve(u0_wrong, T=1.0, dt=0.1)
    u0_right = np.array([1.0])
    result = model.solve(u0_right, T=1.0, dt=0.1)
    #Check number of dimensions is 1
    assert result.time.ndim == 1
    #Check if the state variable u has one state
    assert result.solution.shape[0] == 1

@pytest.mark.parametrize("a,u0_s,T,dt", TEST_CASES)
def test_solve_time(a: float, u0_s: float, T: float, dt: float) -> None:
    """
    Check that time grid starts at 0, ends at T, and steps by dt.
    """
    model = ExponentialDecay(a)
    u0 = np.array([u0_s], dtype=float)

    result = model.solve(u0, T=T, dt=dt)
    result_time = result.time

    #Sanity checks for dimensions and length
    assert result_time.ndim == 1
    assert len(result_time) >= 2

    #Assert the checkpoints exactly and also the steps
    #The first time point is zero
    assert result_time[0] == pytest.approx(0.0, rel=0, abs=1e-12)
    #The last time point is T
    assert result_time[-1] == pytest.approx(T, rel=0, abs=1e-12)
    #The difference between the second and first time point is dt.
    assert (result_time[1] - result_time[0]) == pytest.approx(dt, rel=0, abs=1e-12)

@pytest.mark.parametrize("a,u0_s,T,dt", TEST_CASES)
def test_solve_solution(a: float, u0_s: float, T: float, dt: float) -> None:
    model = ExponentialDecay(a)
    #The initialized 1-element np array
    u0 = np.array([u0_s], dtype=float)

    #Solving the ODE with end time T and step dt
    result = model.solve(u0, T=T, dt=dt)
    #Extracting the time points
    result_time = result.time
    #result.solution = (num_states, num_time_points)
    #   result.solution[0] = num_states
    y = result.solution[0]
    #We compute the exact solution at the given time point
    y_exact = u0_s * np.exp(-a*result_time)

    #Computing the rel_err between num and exact solution
    relative_error = np.linalg.norm(y - y_exact) / np.linalg.norm(y_exact)
    #Checking for 1% or less difference
    assert relative_error <= 0.01