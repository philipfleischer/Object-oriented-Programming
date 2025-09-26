"""
test_double_pendulum.py
=======================

This file contains unit tests for the 'DoublePendulum' class.
The double pendulum is a nonlinear and chaotic system, so correctness 
of the equations of motion is verified using carefully chosen test 
cases with known expected results.

Overview of Tests:
1. test_domega1_dt
   - Parameterized test for verifying that the derivative of ω1 (angular
     velocity of pendulum 1) is computed correctly.
   - Uses several combinations of θ1 and θ2 while keeping ω1 and ω2 fixed.
   - Checks both dθ1/dt = ω1 and the expected value of dω1/dt.
2. test_domega2_dt
   - Parameterized test for verifying that the derivative of ω2 (angular
     velocity of pendulum 2) is computed correctly.
   - Similar setup as 'test_domega1_dt' but checks dθ2/dt and dω2/dt.

Structure
- Both tests use 'pytest.mark.parametrize' to efficiently test multiple
  inputs and expected results in a compact manner.
- Each test creates a 'DoublePendulum' instance, sets the initial state
  vector '(θ1, ω1, θ2, ω2)', and calls the model.
- Assertions use 'numpy.isclose' to account for floating-point precision
  in the computed derivatives.

Dependencies
- numpy
- pytest
- double_pendulum

Run all tests with:
    pytest test_double_pendulum.py -v
To run a specific test (example):
    pytest test_double_pendulum.py -k test_domega1_dt
"""


import numpy as np
import pytest
from double_pendulum import *


@pytest.mark.parametrize(
    "theta1, theta2, expected",
    [
        (0, 0, 0),
        (0, 0.5, 3.386187037),
        (0.5, 0, -7.678514423),
        (0.5, 0.5, -4.703164534),
    ],
)
def test_domega1_dt(theta1: float, theta2: float, expected: float) -> None:
    """
    Function for testing that domega_1/dt is computed correctly.

    Run test:
        pytest test_double_pendulum.py::test_domega1_dt
    """
    model = DoublePendulum()
    t = 0
    y = (theta1, 0.25, theta2, 0.15)
    dtheta1_dt, domega1_dt, _, _ = model(t, y)
    assert np.isclose(dtheta1_dt, 0.25)
    assert np.isclose(domega1_dt, expected)


@pytest.mark.parametrize(
    "theta1, theta2, expected",
    [
        (0, 0, 0.0),
        (0, 0.5, -7.704787325),
        (0.5, 0, 6.768494455),
        (0.5, 0.5, 0.0),
    ],
)
def test_domega2_dt(theta1: float, theta2: float, expected: float) -> None:
    """
    Function for testing that domega_2/dt is computed correctly

    Run test:
        pytest test_double_pendulum.py::test_domega2_dt
    """
    model = DoublePendulum()
    t = 0
    y = (theta1, 0.25, theta2, 0.15)
    _, _, dtheta2_dt, domega2_dt = model(t, y)
    assert np.isclose(dtheta2_dt, 0.15)
    assert np.isclose(domega2_dt, expected)

def test_solve_double_pendulum_zero_ic() -> None:
    """
    Solve the DoublePendulum ODE with zero initial conditions
    for all state variables.

    Run test:
        pytest test_double_pendulum.py::test_solve_double_pendulum_zero_ic
    """
    model = DoublePendulum()
    u0 = np.array([0.0, 0.0, 0.0, 0.0], dtype=float)
    result = model.solve(u0=u0, T=5.0, dt=0.01)
    
    assert result.solution.shape[0] == 4
    assert np.allclose(result.solution, 0.0, rtol=1e-12, atol=1e-12)

  
@pytest.mark.parametrize(
    "L1, L2, g, T, dt",
    [
        (1.0, 1.0, 9.81, 5.0, 0.01),
        (1.5, 0.7, 9.81, 3.0, 0.02),
        (2.0, 1.0, 3.71, 2.0, 0.05),
    ],
)
def test_solve_double_pendulum_function_zero_ic(L1: float, L2: float, g: float, T: float, dt: float) -> None:
    """
    Check that a double pendulum with zero initial conditions stays at rest.

    Run test:
        pytest test_double_pendulum.py::test_solve_double_pendulum_function_zero_ic
    """
    model = DoublePendulum(L1=L1, L2=L2, g=g)
    u0 = np.array([0.0, 0.0, 0.0, 0.0], dtype=float)

    result = model.solve(u0=u0, T=T, dt=dt)

    #All angular states zero
    assert np.allclose(result.theta1, 0.0)
    assert np.allclose(result.omega1, 0.0)
    assert np.allclose(result.theta2, 0.0)
    assert np.allclose(result.omega2, 0.0)

    #Cartesian coordinates
    assert np.allclose(result.x1, 0.0)
    assert np.allclose(result.x2, 0.0)
    assert np.allclose(result.y1, -L1)
    assert np.allclose(result.y2, -(L1 + L2))