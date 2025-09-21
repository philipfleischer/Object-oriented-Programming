import numpy as np
from ode import ODEModel

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