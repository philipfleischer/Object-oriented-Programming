"""
ode.py
======

This module provides the core framework for solving ordinary differential
equations (ODEs) in this project. It defines an abstract base class for
ODE models, a result container for solver output, custom error handling,
and utility functions for plotting solutions and energies.

Contents:
- ODEResult (NamedTuple):
    A lightweight container holding the solution time points and state
    values produced by an ODE solver.
- InvalidInitialConditionError:
    Custom exception raised when invalid initial conditions are passed
    to an ODE model (wrong type, dimension or length).
- ODEModel (abstract base class):
    Defines the common interface for all ODE models in this project.
    All specific models (e.g., exponential decay, pendulum,
    double pendulum) must inherit from this class and implement:
        __call__(t, u): RHS of the ODE system, returning du/dt.
        num_states: Property specifying the number of state variables.
    Concrete subclasses may override _create_result() to return class unique
    result objects (e.g.: coordinates and energies).
- plot_ode_solution(results, state_labels=None, filename=None):
    Generic plotting function for visualizing state over time.
    Works for any ODEResult-like object (e.g: PendulumResults and DoublePendulumResults).
- plot_energy(results, filename=None):
    Generic energy plotting function that works with both
    PendulumResults and DoublePendulumResults (duck typing). It only
    relies these attributes, being provided:
        - time
        - potential_energy
        - kinetic_energy
        - total_energy
    This demonstrates polymorphism through duck typing: the function
    does not care about the class type of the input, only that it
    "quacks like a duck."

Design Notes:
- The ODEModel class enforces a clean interface using Python's
  abc (Abstract Base Classes). This ensures all derived classes
  explicitly define their equations of motion and number of states.
- The solve() method centralizes calls to SciPy's solve_ivp, performing
  validation of inputs and delegating postprocessing to _create_result().
- Utility functions are defined at module level to avoid duplication.
  For example, plot_energy is shared across single and double pendulum
  models, avoiding repeated code while still supporting polymorphism.

This file is the backbone of the project. It allows specific ODE models
to focus only on their unique mathematics while reusing common solving
and plotting infrastructure.

Run file with:
    python ode.py
"""

import numpy as np
import abc
from typing import NamedTuple, Any, Optional
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


class ODEResult(NamedTuple):
    """The result of solving an ODE.

    Args:
        time (np.ndarray): The time steps solved for
        solution (np.ndarray): The solution of the problem at the given times.
    """

    time: np.ndarray
    solution: np.ndarray

    @property
    def num_states(self) -> int:
        """
        Number of state variables.

        Returns
            int
        """
        return int(self.solution.shape[0])

    @property
    def num_timepoints(self) -> int:
        """
        Number of time points.

        Returns
            int
        """
        return int(self.solution.shape[1])


class InvalidInitialConditionError(RuntimeError):
    """
    Raised when the initial condition u0 has the wrong shape/type.
    """

    pass


class ODEModel(abc.ABC):
    """
    Common interface for all ODE's (ordinary differntial equations).
    Can not be used directly - have to be inherited and it must
    be implemented a solution for a particular type of ODE.
    """

    @abc.abstractmethod
    def __call__(self, t: float, u: np.ndarray) -> np.ndarray:
        """
        Calculate right side of the diff equation du/dt = f(t, u).
        Must be implemented from classes that inherits, or
        else we will get NotImplementedError.
        """
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def num_states(self) -> int:
        """
        Tells how many variables the system keeps track of.

        For example, in the exponential decay model there is only one
        variable (u). More complicated models can have several variables
        changing over time. Each of these is counted as a 'state'.

        Returns
            int
        """
        raise NotImplementedError

    def _create_result(self, solution: Any) -> Any:
        """
        Converts the raw output from the mathematical solver into a simple
        result with two parts.
        1. Time: The points in time where the solution was calculated.
        2. Solution: The values of the system at those time points.

        This makes the result easier to work with and understand.

        Returns
            Any
        """
        if not hasattr(solution, "t") or not hasattr(solution, "y"):
            raise AttributeError("Solution object must have attributes t and y")
        return ODEResult(time=solution.t, solution=solution.y)

    def solve(self, u0: np.ndarray, T: float, dt: float, method: str = "RK45") -> Any:
        """
        solve() works out how the systen develops over time.

        Parameters to give the funciton solve_ivp from scipy:
        u0:
            The starting values or initial conditions.
        T:
            How long we want it to simulate.
        dt:
            How often we want results (time steps).
        method:
            Which numerical method to use (Default is RK45).

        Validates that u0 matches the model's number of states.

        solve() returns the times and the corresponding values of the system,
        so we can inspect or plot how the system changes over time.

        Returns
            Any
        """
        if T < 0:
            raise ValueError("T must be positive.")
        if dt <= 0:
            raise ValueError("dt must be positive.")
        if not isinstance(u0, np.ndarray):
            raise InvalidInitialConditionError("u0 must be a numpy.ndarray")
        if u0.ndim != 1:
            raise InvalidInitialConditionError("u0 must be a 1D numpy array.")
        if len(u0) != self.num_states:
            raise InvalidInitialConditionError(
                f"u0 has length {len(u0)} but model expects {self.num_states} states"
            )

        t_eval = np.arange(0, T + dt, dt)
        solution = solve_ivp(self, (0, T), u0, t_eval=t_eval, method=method)
        return self._create_result(solution)


def plot_ode_solution(
    results: ODEResult,
    state_labels: Optional[list[str]] = None,
    filename: Optional[str] = None,
) -> None:
    """
    Plotting the solution of an ODE system.

    Parameters:
    results:
        ODEResult
            Ouput from ODEModel.solve(), must have:
                result.time: 1D array of time points T
                result.solution: 2D array with shape num_states and T
    state_labels:   list[str] | None, optional
        Labels for each state.
    filename:   str | None, optional
        If not None, the plot is saved to file path.
        Else: plot window is displayed.

    Returns
        None
    """
    result_time = np.array(results.time)

    solu = np.array(results.solution)
    # If solu is a 1D, we reshape it to 2D array here
    if solu.ndim == 1:
        solu = solu.reshape(1, -1)

    # num_states, num_time = solu.shape
    # extracting number of states (rows) and num time points (column)
    num_states = getattr(results, "num_states", solu.shape[0])
    num_time = getattr(results, "num_timepoints", solu.shape[1])
    if result_time.ndim != 1 or result_time.shape[0] != num_time:
        raise ValueError(
            "result.time must be a 1D and match result.solutions time dimension."
        )

    if state_labels is None:
        # If no labels, we construct them for {"State1", "State2", ... "StateK"}
        labels = [f"State {i + 1}" for i in range(num_states)]
    else:
        if len(state_labels) != num_states:
            raise ValueError(
                f"state_labels length ({len(state_labels)}) must be equal to the number of states: ({num_states})."
            )
        labels = state_labels

    # Plotting the figure:
    # Instantiate the figure
    plt.figure()
    # Plot in the states and time points
    for i in range(num_states):
        plt.plot(result_time, solu[i, :], label=labels[i])

    plt.xlabel("Time")
    plt.ylabel("State Value")
    plt.grid(True, which="both", linestyle="--", alpha=0.4)
    plt.legend()

    if filename:
        plt.savefig(filename, dpi=150, bbox_inches="tight")
        plt.close()
    else:
        plt.show()


def plot_energy(results: Any, filename: Optional[str] = None) -> None:
    """
    This function plots the potential, kinetic, and
    total energy of a pendulum system.
    plot_energy() works for both single and double pendulum
    system results. It uses 'duck typing' which means that it
    only relies on the attributes, namely - time, potential_energy,
    kinetic_energy and total_energy, rather than the class types.
    The function will work as long as it is provided with these
    attributes.

    Parameters:
    results: Any
        A result object with the attributes:
            time (np.ndarray): array of time points.
            potential_energy (np.ndarray)
            kinetic_energy (np.ndarray)
            total_energy (np.ndarray)
        Ex: PendulumResults and DoublePendulumResults
    filename: str or None, Optional
        If provided, plot saved to filename
        If not provided, plot window displayed

    Returns
        None
    """
    t = results.time
    P = results.potential_energy
    K = results.kinetic_energy
    E = results.total_energy

    plt.figure()
    plt.plot(t, P, label="Potential Energy")
    plt.plot(t, K, label="Kinetic Energy")
    plt.plot(t, E, label="Total Energy", linewidth=2)

    plt.xlabel("Time [s]")
    plt.ylabel("Energy [J]")
    plt.title("Pendulum Energy VS. Time")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend()

    if filename:
        plt.savefig(filename, dpi=150, bbox_inches="tight")
        plt.close()
    else:
        plt.show()


if __name__ == "__main__":

    # Making test class to instatiate an ODEModel object
    class MinimalDecayTest(ODEModel):
        """Minimal test for ODE."""

        def __call__(self, t: float, u: np.ndarray) -> np.ndarray:
            return np.array([-u[0]])

        @property
        def num_states(self) -> int:
            return 1

    model = MinimalDecayTest()
    result = model.solve(u0=np.array([1.0]), T=2.0, dt=0.1)

    print("Time steps: ", result.time)
    print("Solution steps: ", result.solution)

    plot_ode_solution(result, state_labels=["u(t)"])
