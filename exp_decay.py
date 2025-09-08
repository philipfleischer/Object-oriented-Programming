import numpy as np

class ExponentialDecay:
    """Representerer en difflikning (ODE) på formen:
    du/dt = -au"""
    
    def __init__(self, a: float):
        """a er decay-konstanten, kan ikke være negativ (da får mann
        ValueError)."""
        if a < 0:
            raise ValueError(f"ExponentialDecay.__init__: a er negativ ({a})")
        self._a = a


    def __call__(self, t: float, u: np.ndarray[float]) ->np.ndarray[float]:
        """Når vi kallet et objekt som en funksjon regnes du/dt ut for 
        disse verdiene av t og u (u kan være en array med mange elementer,
        og du/dt vil ha like mange elementer).)"""
        du_dt = -self._a * u
        return du_dt