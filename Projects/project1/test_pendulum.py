"""Write how to run this file and what it is about!"""

import numpy as np
import pytest
from pendulum import *

def test_pendulum_derivatives_correct() -> None:
    """
    Check derivatives for:
        L = 1.42
        θ = π/6
        w = 0.35
    """
    L = 1.42
    g = 9.81
    theta = np.pi / 6
    omega = 0.35
    u = np.array([theta, omega], dtype=float)

    model = Pendulum(L=L, g=g)

    #Ecpected: dθ/dt = w
    expected_dtheta = omega
    expected_domega = -(g / L) * np.sin(theta)

    d = model(t=0.0, u=u)
    assert np.isclose(d[0], expected_dtheta, rtol=1e-12, atol=1e-12)
    assert np.isclose(d[1], expected_domega, rtol=1e-12, atol=1e-12)

def test_pendulum_equilibrium_at_rest() -> None:
    """
    At equilibrium (0=0, w=0) the derivatives should be zero
    """
    model = Pendulum(L=1.0, g=9.81)
    u = np.array([0.0, 0.0], dtype=float)
    d = model(t=0.0, u=u)

    assert np.isclose(d[0], 0.0, rtol=1e-12, atol=1e-12)
    assert np.isclose(d[1], 0.0, rtol=1e-12, atol=1e-12)

def test_solve_pendulum_ode_with_zero_ic() -> None:
    """
    if u0 = (0,0), both theta and omega should remain zero.
    """
    model = Pendulum()  #Default values for now
    u0 = np.array([0.0, 0.0], dtype=float)
    result = model.solve(u0=u0, T=5.0, dt=0.01)

    #result.solution: (num_states, num_times)
    theta = result.solution[0]
    omega = result.solution[1]

    #Check if theta and omega consists of 0's
    assert np.allclose(theta, 0.0)
    assert np.allclose(omega, 0.0)