import numpy as np
import abc
#Sier at ODEModel skal arve fra abc:
class ODEModel(abc.ABC):
    """Felles grensesnitt for alle ODE'er (ordinære difflikninger).
    Kan ikke brukes direkte - må arves fra og det må implementeres
    en løsningsmetode for en bestemt type ODE. """
    
    def __call__(self, t: float, u: np.ndarray) -> np.ndarray:
        """Regne ut høre side (RHS) av difflikningen du/dt = f(t, u).
        Må implemeneteres av klasser som arver herfra, ellers får du 
        NotImplementetError. """
        raise NotImplementedError
    