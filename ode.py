import numpy as np
import abc
from typing import NamedTuple, Any
from scipy.integrate import solve_ivp

class ODEResult(NamedTuple):
    """The result of solving an ODE.
    
    Args:
        time (np.ndarray): The time steps solved for
        solution (np.ndarray): The solution of the problem at the given times.
    """
    time: np.ndarray
    solution: np.ndarray

class InvalidInitialConditionError(RuntimeError):
    """
    Raised when the initial condition u0 has the wrong shape/type.
    """
    pass
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
        """
        Tells how many variables the system keeps track of.
        
        For example, in the exponential decay model there is only one
        variable (u). More complicated models can have several variables
        chanigng over time. Each of these is counted as a 'state'."""
        raise NotImplementedError
    
    def _create_result(self, solution: Any) -> ODEResult:
        """
        Converts the raw output from the mathematical solver into a simple 
        result with two parts.
        1. Time: The points in time where the solution was calculated.
        2. Solution: The values of the sustem at those time.

        This makes the result easier to work with and understand.
        """
        if not hasattr(solution, "t") or not hasattr(solution, "y"):
            raise AttributeError("Solution object must have attributes t and y")
        return ODEResult(time=solution.t, solution=solution.y)
    
    def solve(self, u0: np.ndarray, T: float, dt: float, method: str = "RK45") -> ODEResult:
        """
        Works out how the systen develops over time.
        
        Parameters to give the funciton solve_ivp from scipy:
        - u0: The starting values or initial conditions.
        - T: How long we want it to simulate.
        - dt: How often we want results (time steps).
        - method: Which numerical method to use (Default is RK45).

        Validates that u0 matches the model's number of states.

        solve() reutrns the times and the corresponding values of the system,
        so we can inspect or plot how the system changes over time.
        """

        if not isinstance(u0, np.ndarray): raise InvalidInitialConditionError("u0 must be a numpy.ndarray")
        if u0.ndim != 1: raise InvalidInitialConditionError("u0 must be a 1D numpy array.")
        if len(u0) != self.num_states:
            raise InvalidInitialConditionError(
                f"u0 has length {len(u0)} but model expects {self.num_states} states"
            )

        t_eval = np.arange(0, T + dt, dt)
        solution = solve_ivp(self, (0, T), u0, t_eval=t_eval, method=method)
        return self._create_result(solution)
