"""
Tests for the ExponentialDecay ODE model (exp_decay.py).

This file contains unit tests for the ExponentialDecay class and its integration
with the shared ODE framework (ode.py). The tests are implemented using pytest
and focus on verifying correctness, robustness, and reproducibility.

Contents:
1. test_rhs
    - Verifies that the right-hand side (RHS) of the ODE (du/dt = -a*u) is computed
      correctly for a known input.
2. test_negative_decay_raises_ValueError_constructor
    - Ensures that creating an ExponentialDecay model with a negative decay constant
      raises a ValueError.
3. test_negative_decay_raises_ValueError
    - Ensures that setting the decay constant to a negative value after construction
      raises a ValueError.
4. test_num_states
    - Verifies that the model reports the correct number of states (1).
    - Ensures the property cannot be reassigned.
5. test_solve_with_different_number_of_initial_states
    - Checks that the solver raises an InvalidInitialConditionError when the
      initial condition array has the wrong shape.
    - Verifies that solving with a correct initial condition returns results
      with valid shapes for time and solution.
6. test_solve_time (parameterized)
    - Ensures that the time grid returned by the solver starts at 0, ends at T,
      and increments consistently by dt.
7. test_solve_solution (parameterized)
    - Compares the numerical solution with the exact analytical solution
      u(t) = u0 * exp(-a*t).
    - Verifies that the relative error is ≤ 1%.
8. test_plot_ode_solution_saves_file
    - Tests that the plotting function plot_ode_solution saves a PNG file
      to disk when a filename is provided.
    - Confirms that the file is created and deletes it after the test.

Dependencies:
- numpy
- pytest
- pathlib
- matplotlib

How to run:
Execute all tests with:
    pytest test_exp_decay.py
To run a specific test (example):
    pytest test_exp_decay.py::test_rhs
"""

import numpy as np
import pytest
from pathlib import Path
from typing import List, Tuple
from exp_decay import ExponentialDecay
from ode import InvalidInitialConditionError, plot_ode_solution


#Cases for testing: (a, u0_scalar, T, dt)
TEST_CASES: List[Tuple[float, float, float, float]] = [
    (0.4, 3.2, 10.0, 0.01),
    (1.0, 2.0, 2.0, 0.05),
    (0.2, 1.5, 5.0, 0.10)
]

#Test right hand side = test_rhs
def test_rhs() -> None:
    """
    Testing right hand side (RHS) of the diff equation du/dt = -au
    
    Run with: 
        pytest test_exp_decay.py::test_rhs
    """
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
    """
    Run with: 
        pytest test_exp_decay.py::test_negative_decay_raises_ValueError_constructor
    """
    a = -1.0
    with pytest.raises(ValueError):
        should_fail = ExponentialDecay(a)

def test_negative_decay_raises_ValueError() -> None:
    """
    Run with: 
        pytest test_exp_decay.py::test_negative_decay_raises_ValueError
    """
    a = 0.4
    model = ExponentialDecay(a)
    with pytest.raises(ValueError):
        model.decay = -1.0

def test_num_states() -> None:
    """
    Run with: 
        pytest test_exp_decay.py::test_num_states
    """
    a = 0.4
    model = ExponentialDecay(a)
    assert model.num_states == 1
    with pytest.raises(AttributeError):
        model.num_states = 2
    
def test_solve_with_different_number_of_initial_states() -> None:
    """
    Run with: 
        pytest test_exp_decay.py::test_solve_with_different_number_of_initial_states
    """
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
    #Checking property num_states for the ODERESULT class
    assert result.num_states == 1

@pytest.mark.parametrize("a,u0_s,T,dt", TEST_CASES)
def test_solve_time(a: float, u0_s: float, T: float, dt: float) -> None:
    """
    Check that time grid starts at 0, ends at T, and steps by dt.
    
    Run with:
        pytest test_exp_decay.py::test_solve_time
    """
    model = ExponentialDecay(a)
    u0 = np.array([u0_s], dtype=float)

    result = model.solve(u0, T=T, dt=dt)
    result_time = result.time

    #Sanity checks for dimensions and length
    assert result_time.ndim == 1
    assert len(result_time) >= 2

    assert len(result.time) == result.num_timepoints

    #Assert the checkpoints exactly and also the steps
    #The first time point is zero
    assert result_time[0] == pytest.approx(0.0, rel=0, abs=1e-12)
    #The last time point is T
    assert result_time[-1] == pytest.approx(T, rel=0, abs=1e-12)
    #The difference between the second and first time point is dt.
    assert (result_time[1] - result_time[0]) == pytest.approx(dt, rel=0, abs=1e-12)

@pytest.mark.parametrize("a,u0_s,T,dt", TEST_CASES)
def test_solve_solution(a: float, u0_s: float, T: float, dt: float) -> None:
    """
    Run with:
        pytest test_exp_decay.py::test_solve_solution
    """
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

def test_plot_ode_solution_saves_file() -> None:
    """
    Run with:
        pytest test_exp_decay.py::test_plot_ode_solution_saves_files
    """
    #initialize the test file, experiment now
    #filename = Path("exponential_decay.png")
    filename = Path("test_plot.png")

    #Check if the file is already existing
    if filename.is_file():
        filename.unlink()

    model = ExponentialDecay(0.4)
    u0 = np.array([2.0])
    result = model.solve(u0, T=2.0, dt=0.1)

    #Here we call the plotting funciton we want to test
    plot_ode_solution(results=result, state_labels=["u"], filename=filename)

    #Check the file is created
    assert filename.is_file()
    #Delete the file
    filename.unlink()