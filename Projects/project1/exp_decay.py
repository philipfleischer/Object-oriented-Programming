"""
exp_decay.py
============

This module implements a simple model of exponential decay using the
object-oriented ODE framework defined in 'ode.py'.

The exponential decay is described by the first-order ODE:
    du/dt = -a * u

where:
    - u(t) is the decaying quantity,
    - a ≥ 0 is the decay constant controlling how fast u decreases.

Contents:
- ExponentialDecay:
    A class that inherits from ODEModel and represents the exponential
    decay system. It provides:
        - A constructor that validates the decay constant.
        - A __call__ method implementing the right-hand side of the ODE.
        - A property 'decay' with getter and setter for validation.
        - A 'num_states' property returning 1 (since the model only has one state).

Usage:
This file can be run directly. When executed, it creates an instance of
ExponentialDecay with a = 0.4, solves the ODE with initial condition
u0 = 4.0 over T = 10 seconds with timestep dt = 0.01, and saves the
resulting trajectory to the file 'exponential_decay.png'.

Run file with:
    python exp_decay.py

Dependencies:
- numpy
- scipy.integrate.solve_ivp
- matplotlib
- ode.py
"""

import numpy as np
from ode import ODEModel, ODEResult, plot_ode_solution
import scipy as sp
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


# ExponentialDecay inherits from ODEModel
class ExponentialDecay(ODEModel):
    """
    A simple model of exponential decay.
    This represents the differntial equation (ODE):
        du/dt = -au
    Where 'u' is the quantity that decays, and 'a' is the decay constant.
    """

    def __init__(self, a: float) -> None:
        """
        Creates a new exponential decay model.

        Parameters:
        a:  float
            The decay constant. It controls how fast 'u' decays.
            It must positive, otherwise a value error is raised.
        """
        if a < 0:
            raise ValueError("decay constant cannot be a negative integer value")
        self.decay = a

    def __call__(self, t: float, u: np.ndarray[float]) -> np.ndarray[float]:
        """
        Calculates how quickly the system changes at a given time.

        Paraters:
        t:  float
            The time at which to evaluate the rate of change.
        u:  np.ndarray
            The rate of change that du/dt has at this time and state.

        Return
            np.ndarray[float]
        """
        du_dt = -self.decay * u
        return du_dt

    # With this, the decay works as a variable instead of a function
    @property
    def decay(self) -> float:
        """
        The decay constant 'a'.

        This class property tells us how quickly the quantity
        decays, where larger values results in faster decays.

        Return
            float
        """
        return self._a

    @decay.setter
    def decay(self, value: float) -> None:
        """
        Sets a new value for the decay constant.

        Parameters:
        value:  float
                The new decay constant given, must be positive.

        Raises:
        ValueError -> If value is negative.

        Returns:
            None
        """
        if value < 0:
            raise ValueError(f"ExponentialDecay.__init__: value is negative ({value})")
        self._a = value

    @property
    def num_states(self) -> int:
        """
        The number of state variabels in the model is returned.
        The Exponential decay ODE only has one state var (u), returns 1.

        Return
            int

        """
        return 1


if __name__ == "__main__":
    model = ExponentialDecay(0.4)
    result = model.solve(u0=np.array([4.0]), T=10.0, dt=0.01)
    print(type(result))
    plot_ode_solution(
        results=result, state_labels=["u"], filename="exponential_decay.png"
    )
