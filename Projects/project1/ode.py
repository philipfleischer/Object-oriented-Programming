import numpy as np
import abc
#Sier at ODEModel skal arve fra abc:
class ODEModel(abc.ABC):
    """
    Common interface for all ODE´s (ordinary differntial equations).
    Can not be used directly - have to be inherited and it must
    be implemented a solution for a particular type of ODE."""
    
    @abc.abstractmethod
    def __call__(self, t: float, u: np.ndarray) -> np.ndarray:
        """
        Calculate right side of the diff equation du/dt = f(t, u).
        Must be implemented from classes that inherits, or
        else we will get NotImplementedError."""
        raise NotImplementedError
    
    def num_states(self) -> int:
        """Number of state variables in a ODE system.
        This will differ on from different ODEModels."""
        raise NotImplementedError


    