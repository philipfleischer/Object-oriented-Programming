import numpy as np
from ode import ODEModel, ODEResult, plot_ode_solution
import scipy as sp
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#ExponentialDecay inherits from ODEModel
class ExponentialDecay(ODEModel):
    """
    A simple model of exponential decay.
    This represents the differntial equation (ODE):
        du/dt = -au
    Where 'u' is the quantity that decays, and 'a' is the decay constant.
    """
    
    def __init__(self, a: float):
        """
        Creates a new exponential decay model.

        Parameters:
        a:  float
            The decay constant. It controls how fast 'u' decays.
            It must be non-negative, otherwise an error is raised.
        """
        if a < 0: raise ValueError("decay constant cannot be a negative integer value")
        self.decay = a


    def __call__(self, t: float, u: np.ndarray[float]) -> np.ndarray[float]:
        """
        Calculates how quickly the system changes at a given time.
        
        Paraters:
        t:  float
            The time at which to evaluate the rate of change.
            (Note: 't' is not actually used here because we do not
            depend on the time variabel directly).
        u:  np.ndarray
            The rate of change that du/dt has at this time and state.
        """
        du_dt = -self.decay * u
        return du_dt

    #With this, the decay works as a variable instead of a function
    @property
    def decay(self) -> float:
        """
        The decay constant 'a'.

        This class property tells us how quickly the quantity
        decays, where larger values results in faster decays.
        """
        return self._a

    @decay.setter
    def decay(self, value: float) -> None:
        """
        Sets a new value for the decay constant.

        Parameters:
        value:  float
                The new decay constant given, must be Non-Negative.
        
        Raises:
        ValueError -> If value is negative.
        """
        if value < 0:
            raise ValueError(f"ExponentialDecay.__init__: value is negative ({value})")
        self._a = value

    @property
    def num_states(self) -> int:
        """
        The number of state variabels in the model is returned.
        The Exponential decay ODE only has one state var (u), so
        it always returns 1.
        """
        return 1


if __name__ == "__main__":
    """eksempel = ExponentialDecay(2.0)
    print(eksempel.decay)

    #Parameter setup:
    a = 0.4
    model = ExponentialDecay(a)

    #Initial condition and time span
    u0 = np.array([3.2])
    T = 10.0
    dt = 0.01
    result = model.solve(u0, T=10, dt=0.01)

    #Plotting the result and solution into a figure
    plt.plot(result.time, result.solution[0], label="Decay")
    plt.xlabel("t")
    plt.ylabel("u(t)")
    plt.legend()
    plt.show()"""
    model = ExponentialDecay(0.4)
    result = model.solve(u0=np.array([4.0]), T=10.0, dt=0.01)
    print(type(result))
    plot_ode_solution(results=result, state_labels=["u"], filename="exponential_decay.png")
    