"""Tests for the single pendulum ODE model with parametrization."""

import numpy as np
import pytest
from pendulum import *

#Derivatives test
@pytest.mark.parametrize(
    "L,g,theta,omega",
    [   (1.42, 9.81, np.pi/6, 0.35),
        (1.00, 9.81, np.pi/4, 1.20),
        (2.50, 3.81, np.pi/8, -0.10) ]
)
def test_pendulum_derivatives_correct(L: float, g: float, theta: float, omega: float) -> None:
    """
    Check that the RHS matches for different derivate values.
    """
    u = np.array([theta, omega], dtype=float)
    model = Pendulum(L=L, g=g)

    #Ecpected: dθ/dt = w
    expected_dtheta = omega
    expected_domega = -(g / L) * np.sin(theta)

    d = model(t=0.0, u=u)
    assert np.isclose(d[0], expected_dtheta, rtol=1e-12, atol=1e-12)
    assert np.isclose(d[1], expected_domega, rtol=1e-12, atol=1e-12)

#Equilibrium test
@pytest.mark.parametrize(
    "L,g",
    [   (1.0, 9.81),
        (0.75, 9.81),
        (2.0, 3.81) ]
)
def test_pendulum_equilibrium_at_rest(L: float, g: float) -> None:
    """
    At equilibrium (0=0, w=0) the derivatives should be zero
    """
    model = Pendulum(L=L, g=g)
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

#Test solve with zero ICs
@pytest.mark.parametrize(
    "L,g,T,dt",
    [   (1.0, 9.81, 5.0, 0.01),
        (2.0, 9.81, 3.0, 0.05),
        (0.5, 1.62, 2.0, 0.02) ]
)
def test_solve_pendulum_function_zero_ic(L: float, g: float, T: float, dt: float) -> None:
    model = Pendulum(L=L, g=g)
    u0=np.array([0.0, 0.0], dtype=float)
    result = model.solve(u0=u0, T=T, dt=dt)

    #Theta and omega must remain zero
    assert np.allclose(result.theta, 0.0)
    assert np.allclose(result.omega, 0.0)

    #Cartesion x -> 0
    assert np.allclose(result.x, 0.0)
    #Cartesion y -> -L
    assert np.allclose(result.y, -L)

@pytest.mark.parametrize(
    "L,g,u0,T,dt",
    [   (1.0, 9.81, np.array([0.0, 0.0]), 2.0, 0.01),
        (2.0, 9.81, np.array([0.1, 0.2]), 3.0, 0.01),  ]
)
def test_pendulum_energy_and_velocities(L: float, 
                                        g: float, 
                                        u0: float, 
                                        T: float, 
                                        dt: float) -> None:
    model = Pendulum(L=L, g=g)
    result = model.solve(u0=u0, T=T, dt=dt)

    #Checking that each property can be computed and returns
    # correct shapes for (potential_energy, vy, vx, kinetic_energy)
    assert result.potential_energy.shape == result.time.shape
    assert result.vx.shape == result.time.shape
    assert result.vy.shape == result.time.shape
    assert result.kinetic_energy.shape == result.time.shape
    assert result.total_energy.shape == result.time.shape