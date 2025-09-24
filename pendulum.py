"""
pendulum.py
===========

This module implements classes and helper functions for modeling and solving 
the dynamics of a simple pendulum and its dampened variant using ordinary 
differential equations (ODEs).

Core components:
1. **PendulumResults (dataclass)**
   - Stores the solution of the pendulum problem after numerical integration.
   - Contains time array, state array (θ, ω), and pendulum parameters (L, g).
   - Provides convenient properties:
     - 'theta', 'omega': angular displacement and velocity over time.
     - 'x', 'y': Cartesian coordinates of the pendulum bob.
     - 'vx', 'vy': Cartesian velocities (computed via 'np.gradient').
     - 'potential_energy', 'kinetic_energy', 'total_energy': derived energy values.
2. **Pendulum (ODEModel subclass)**
   - Models a single undamped pendulum with length 'L' and gravity 'g'.
   - Implements:
     - '__call__': right-hand side of the ODE system:
         dθ/dt = ω,
         dω/dt = -(g/L) * sin(θ).
     - 'num_states': always 2 (θ and ω).
     - '_create_result': wraps the solver output into a 'PendulumResults' object.
     - 'plot_energy': plots potential, kinetic, and total energy vs. time.
3. **DampenedPendulum (Pendulum subclass)**
   - Extends the simple pendulum with a linear damping term 'B':
         dθ/dt = ω,
         dω/dt = -(g/L) * sin(θ) - B*ω.
   - Useful for simulating more realistic pendulum behavior where energy is not conserved.

Exercises implemented:
- **exercise_2b**: Solve the simple pendulum with initial conditions θ = π/6, ω = 0.35,
  simulate for T=10 s, dt=0.01, and save the solution plot to 'exercise_2b.png'.
- **exercise_2g**: Solve the simple pendulum as above and plot energy curves,
  saving to 'energy_single.png'.
- **exercise_2h**: Solve the dampened pendulum with damping B=1.0 and save the 
  energy plot to 'energy_damped.png'.

Usage:
This file can be run directly. When executed as a script, it will:
- Create and solve a sample Pendulum model,
- Verify that the result is stored as a 'PendulumResults' object,
- Run exercises 2b, 2g, and 2h, saving plots to the current directory.

Dependencies:
- numpy
- matplotlib
- scipy (for numerical integration via 'solve_ivp')
- ode.py (provides the abstract ODEModel base class and plotting utilities)
"""

import numpy as np
from typing import Final, Any, Optional
from dataclasses import dataclass
from ode import *

DEFAULT_G: Final[float] = 9.81

@dataclass
class PendulumResults:
    """Results from solving the pendulum problem.
    
    Args:
        time (np.ndarray): The timesteps of the solution.
        solution (np.ndarray): The values of the solution at the given timesteps.
        L (float): The length of the pendulum rod.
        g (float): The gravitational acceleration.
    """
    time: np.ndarray
    solution: np.ndarray
    L: float
    g: float

    @property
    def theta(self) -> np.ndarray:
        """
        The angular displacement over time.
        """
        return self.solution[0]

    @property
    def omega(self) -> np.ndarray:
        """
        The angular velocity over time.
        """
        return self.solution[1]
    
    @property
    def x(self) -> np.ndarray:
        """
        Computes the horizontal position of the pendulum (x-axis).
        Returns: 
            np.ndarray - array of x coordinates for the time steps.
        """
        return self.L * np.sin(self.theta)

    @property
    def y(self) -> np.ndarray:
        """
        Computes the vertical position of the pendulum (x-axis).
        Returns: 
            np.ndarray - array of x coordinates for the time steps.
        """
        return -self.L * np.cos(self.theta)

    @property
    def potential_energy(self) -> np.ndarray:
        """
        Potential energy: P(t) = g * (y + L) = g*L*(1 - cos theta).
        Sero at the lowest point.
        """
        return self.g * (self.y + self.L)
    
    @property
    def vx(self) -> np.ndarray:
        """
        x-velocity v_x(t) = dx/dt.
        Uses np.gradient with time points array.
        """
        return np.gradient(self.x, self.time)
    
    @property
    def vy(self) -> np.ndarray:
        """
        y-velocity v_y(t) = dy/dt.
        """
        return np.gradient(self.y, self.time)
    
    @property
    def kinetic_energy(self) -> np.ndarray:
        """
        Kinetic energy K(t) = dy/dt.
        """
        return 0.5 * (self.vx**2 + self.vy**2)
    
    @property
    def total_energy(self) -> np.ndarray:
        """
        Total energy: Potential energy + Kinetic energy.
        E(t) = P(t) + K(t).
        """
        return self.potential_energy + self.kinetic_energy


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
    def __init__(self, *, L: float=1.0, g: float=DEFAULT_G) -> None:
        if L <= 0: raise ValueError("Pendulum length L must be a positivie integer.")
        if g < 0: raise ValueError("Gravitational acceleration g must be positive.")
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
    
    def _create_result(self, solution: Any) -> PendulumResults:
        """
        This method converts the raw numerical solution from SciPy into a
        PendulumResults object.
        
        The SciPy function solve_ivp returns a complicated object, since we
        only need time points and solution values, we use _create_result()
        to extract fields and combine them wit L and g, thereby making a 
        simpler and defined data class to store the data in.

        When returning PendulumResults object, it is tied to the current
        Pendulum object. This results in us having a fast and efficient 
        way of accessing theta and omega, and also to the time points and
        solution points.

        Parameters:
        solution: Any
            The result from scipy.integrate.solve_ivp:
                t: np.array of time points
                y: np.array of solution values
        
        Return:
            PendulumResults: time, solution and pendulum params
        
        Raises:
            AttributeError: If .t and .y is not correct in Pendulum object
        """
        if not hasattr(solution, "t") or not hasattr(solution, "y"):
            raise AttributeError("Solution object must have attributes t and y.")
        return PendulumResults(
            time=solution.t, solution=solution.y, L=self.L, g=self.g
        )
    
    
class DampenedPendulum(Pendulum):
    """
    Dampened singled pendulum:
        dθ/dt = ω
        dω/dt = -(g/L)*sin(θ)-B*ω
    
    This class inherits from Pendulum and adds the damping 
    parameter B, also overrides RHS.
    """
    def __init__(self, *, L: float=1.0, g:float=DEFAULT_G, B: float=1.0) -> None:
        super().__init__(L=L, g=g)
        if B < 0: raise ValueError("Damping B can not be negative")
        self._B = float(B)
    
    @property
    def B(self) -> float:
        """
        Linear damping coefficient.
        """
        return self._B

    def __call__(self, t: float, u: np.ndarray) -> np.ndarray:
        """
        RHS for the damped pendulum.
        
        Parameters:
        t: float
            Time
        u: np.ndarray
            State vector [theta, omega]

        Returns:
            np.ndarray - Derivatives with linear damping.
        """
        theta, omega = u
        dtheta_dt = omega
        domega_dt = -(self.g / self.L) * np.sin(theta) - self.B * omega
        return np.array([dtheta_dt, domega_dt], dtype=float)


def exercise_2b() -> ODEResult:
    """
    Create a Pendulum, solve with u0=[pi/6], T=10, dt=0.01, ans save plot.
    """
    model = Pendulum(L=1.0, g=DEFAULT_G)

    u0 = np.array([np.pi / 6.0, 0.35], dtype=float) #[Tetha, Omega]
    T = 10.0
    dt = 0.01

    result = model.solve(u0=u0, T=T, dt=dt)

    #Latex
    state_labels = [r"$\theta$", r"$\omega$"]
    plot_ode_solution(results=result, state_labels=state_labels, filename="exercise_2b.png")
    return result

def exercise_2g() -> None:
    """
    Solve the pendulum with u0=(pi/6, 0.35), T=10.0, dt=0.01
    and save the energy plotting to file energy_single.png.
    """
    model = Pendulum(L=1.0, g=DEFAULT_G)
    u0 = np.array([np.pi/6, 0.35], dtype=float)
    result = model.solve(u0=u0, T=10.0, dt=0.01)
    plot_energy(result, filename="energy_single.png")

def exercise_2h() -> None:
    """
    Solve the dampened pendulum with initialized values.
    Save the energy plot to file: energy_damped.png.
    """
    model = DampenedPendulum(L=1.0, g=DEFAULT_G, B=1.0)
    u0 = np.array([np.pi/6, 0.35], dtype=float)
    result = model.solve(u0=u0, T=10.0, dt=0.01)

    plot_energy(result, filename="energy_damped.png")

if __name__ == "__main__":
    model = Pendulum(L=1.42, g=DEFAULT_G)
    u0 = np.array([np.pi/6, 0.35])
    result = model.solve(u0=u0, T=10, dt=0.01)
    print(isinstance(result, PendulumResults))
    exercise_2b()
    exercise_2g()
    exercise_2h()
