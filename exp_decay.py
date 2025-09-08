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

    #With this, the decay works as a variable instead of a function
    @property
    def decay(self) -> float:
        """Returnerer decay-konstanten a."""
        return self._a

    @decay.setter #Run on writing it in code?
    def decay(self, value: float) -> None:
        """Endrer decay-konstanten a < ValueError hvis ikke positiv verdi"""
        if value < 0:
            raise ValueError(f"ExponentialDecay.__init__: value er negativ ({value})")
        self._a = value

#Eksempel-kode (kjøres ikke ved import)
if __name__ == "__main__":
    eksempel = ExponentialDecay(2.0)
    print(eksempel.decay)