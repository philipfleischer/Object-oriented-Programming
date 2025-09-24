import numpy as np
from typing import Final
from ode import *

DEFAULT_G: Final[float] = 9.81

class Pendulum(ODEModel):
    """
    Single pendulum governed by (teta = θ):
    - dθ/dt = w
    dw/dt = -(g/L) * sin(θ)

    state vector ordering: u = [θ, w]
    θ is the angle (radians), w is the angulat velocity (rad/s).

    Parameters:
    L:  float
        Rod length, must be greater than 0 (Default is 1.0).
    g:  float
        Gravitational accelaration (m/s^2), default 9.81.
    """
    def __init__(self, *, L: float=1.0, g: float=DEFAULT_G):
        if L <= 0: raise ValueError("Pendullum length L must be a positivie integer.")
        if g < 0: raise ValueError("Gravitioanl acceleration g must be positive.")
        self._L = float(L)
        self._g = float(g)
    
    @property
    def L(self) -> float:
        """
        This class property returns the length og the rod in meter.
        """
        return self._L
    
    @property
    def g(self) -> float:
        """
        This class property returns the Gravitational accelaration m/s^2
        """
        return self._g

    @property
    def num_states(self) -> float:
        """
        This class property returns number of states, 
        which should be the number of state variables:
        (θ, w) -> 2
        """
        return 2
    
    def __call__(self, t: float, u: np.ndarray) -> np.ndarray:
        """
        Calculates how the pendulum changes at a given moment in time.
        This function defines the right-hand side of the differential
        equation that describe the pendulum's motion.
        Right-hand side f(t, u) of the ODE system.

        Parameters:
        t:  float
            Time (not used yet?)
        u: np.ndarray
            State vector [θ, w]
        
        Returns:
        np.ndarray
            Derivative vector [dθ/dt, dw/dt].
        """
        #We unpack the vector
        theta, omega = u
        #The derivative of theta with respect to time
        dtheta_dt = omega
        #The derivative of omega with respect to time
        domega_dt = -(self.g / self.L) * np.sin(theta)
        return np.array([dtheta_dt, domega_dt], dtype=float)
