import numpy as np
from ode import ODEModel
import scipy as sp
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#ExponentialDecay inherits from ODEModel
class ExponentialDecay(ODEModel):
    """
    Represents a differntial equation (ODE) on the form:
    du/dt = -au"""
    
    def __init__(self, a: float):
        """
        a is a decay-constant, it can not be negative (-> ValueError)."""
        self.decay = a


    def __call__(self, t: float, u: np.ndarray[float]) -> np.ndarray[float]:
        """
        When we call an object as a function, du/dt will be 
        calculated for the values of t and u (u can be an array
        with many different elements, and du/dt might have common elements)."""
        du_dt = -self.decay * u
        return du_dt

    #With this, the decay works as a variable instead of a function
    @property
    def decay(self) -> float:
        """
        Returns decay-constant a."""
        return self._a

    @decay.setter
    def decay(self, value: float) -> None:
        """
        Changes decay-constant a < ValueError if not positive."""
        if value < 0:
            raise ValueError(f"ExponentialDecay.__init__: value is negative ({value})")
        self._a = value

    @property
    def num_states(self):
        """Exponention decay has one state variable: u."""
        return 1


if __name__ == "__main__":
    eksempel = ExponentialDecay(2.0)
    print(eksempel.decay)

    #Parameter setup:
    a = 0.4
    model = ExponentialDecay(a)

    #Initial condition and time span
    u0 = [3.2]
    T = 10.0
    t_eval = np.arange(0, T, 0.01)

    #This returns an object with .t for time points, 
    # .y for solution arrays, .success to check for 
    # RunTimeErrors, etc.
    results = solve_ivp(model, (0, T), u0, t_eval=t_eval)
    #Solution is the single state ExponentialDecay can be, var u.
    solution = results.y[0]

    #Plotting the result and solution into a figure
    plt.plot(results.t, solution, label="Numerical solution")
    plt.xlabel("t")
    plt.ylabel("u(t)")
    plt.legend()
    plt.show()

    