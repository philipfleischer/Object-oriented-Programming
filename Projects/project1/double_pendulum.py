"""
double_pendulum.py
==================

This module defines the 'DoublePendulum' class, a numerical model for the
classical double pendulum system. It extends the abstract 'ODEModel' from
the 'ode' module and implements the right-hand side of the coupled nonlinear
ODEs that govern the dynamics of two pendulums connected in series.

Overview:
The double pendulum consists of two pendulums with lengths L1 and L2
(simplified here to unit masses M1 = M2 = 1). The system is chaotic and
highly sensitive to initial conditions, making it a well-known example in
nonlinear dynamics.

State vector ordering:
    u = [θ1, ω1, θ2, ω2]

Equations of motion:
    dθ1/dt = ω1
    dθ2/dt = ω2

    dω1/dt = ( L1*ω1²*sin(Δθ)*cos(Δθ)
             + g*sin(θ2)*cos(Δθ)
             + L2*ω2²*sin(Δθ)
             - 2*g*sin(θ1) ) / (2*L1 - L1*cos²(Δθ))

    dω2/dt = ( -L2*ω2²*sin(Δθ)*cos(Δθ)
             + 2*g*sin(θ1)*cos(Δθ)
             - 2*L1*ω1²*sin(Δθ)
             - 2*g*sin(θ2) ) / (2*L2 - L2*cos²(Δθ))

where Δθ = θ2 - θ1 is the relative angle between the pendulums.

Features:
- Handles configurable pendulum lengths (L1, L2) and gravity (g).
- Ensures valid input (positive lengths, nonnegative gravity).
- Provides 'num_states = 4' since the system tracks both angles and
  angular velocities.
- Implements safety against division by zero in denominators by adding
  a small epsilon.

Usage:
The 'DoublePendulum' class is typically used together with the 'solve'
method from the 'ODEModel' base class. 

Dependencies:
- numpy
- ode.py (provides the abstract ODEModel base class and solver interface)
"""

import numpy as np
from typing import Final
from dataclasses import dataclass
from ode import *

DEFAULT_G: Final[float] = 9.81

@dataclass
class DoublePendulumResults:
    """
    Container for double pendulum simulation output
    + system parameters.

    Attributes:
        time (np.ndarray): 1D array of time points.
        solution (np.ndarray): 
            2D array of shape (4, T) with rows: 
                [theta1, omega1, theta2, omega2]
        L1 (float): Length of first pendulum
        L2 (float): Length of second pendulum
        g (float): Gravitational acceleration
    """
    time: np.ndarray
    solution: np.ndarray
    L1: float
    L2: float
    g: float

    #States
    @property
    def theta1(self) -> np.ndarray:
        """
        Returns first theta value.
        """
        return self.solution[0]

    @property
    def omega1(self) -> np.ndarray:
        """
        Returns first omega value.
        """
        return self.solution[1]
    
    @property
    def theta2(self) -> np.ndarray:
        """
        Returns second theta value.
        """
        return self.solution[2]
    
    @property
    def omega2(self) -> np.ndarray:
        """
        Returns second omega value.
        """
        return self.solution[3]
    
    #Cartesian coordinates
    @property
    def x1(self) -> np.ndarray:
        """
        x of mass 1.
        """
        return self.L1 * np.sin(self.theta1)
    
    @property
    def y1(self) -> np.ndarray:
        """
        y f mass 1
        """
        return -self.L1 * np.cos(self.theta1)
    
    @property
    def x2(self) -> np.ndarray:
        """
        x of mass 2 = x1 + L2*sin(theta2).
        """
        return self.x1 + self.L2 * np.sin(self.theta2)
    
    @property
    def y2(self) -> np.ndarray:
        """
        y of mass 2 = y1 + L2*cos(theta2).
        """
        return self.y1 - self.L2 * np.cos(self.theta2)
    
    #Velocities
    @property
    def vx1(self) -> np.ndarray:
        """
        Velocity for x of pendulum 1.
        """
        return np.gradient(self.x1, self.time)

    @property
    def vy1(self) -> np.ndarray:
        """
        Velocity for y of pendulum 1.
        """
        return np.gradient(self.y1, self.time)
    
    @property
    def vx2(self) -> np.ndarray:
        """
        Velocity for x of pendulum 2.
        """
        return np.gradient(self.x2, self.time)
    
    @property
    def vy2(self) -> np.ndarray:
        """
        Velocity for y of pendulum 2.
        """
        return np.gradient(self.y2, self.time)
    
    #Energies
    @property
    def potential_energy(self) -> np.ndarray:
        """
        P = P1 + P2
            P1 = g * (y1 + L1)
            P2 = g * (y2 + L1 + L2)
        """
        P1 = self.g * (self.y1 + self.L1)
        P2 = self.g * (self.y2 + self.L1 + self.L2)
        return P1 + P2
    
    @property
    def kinetic_energy(self) -> np.ndarray:
        """
        K = K1 + K2
            K1 = 0.5 * (y1 + L1)
            K2 = 0.5 * (y2 + L1 + L2)
        """
        K1 = 0.5 * (self.vx1**2 + self.vy1**2)
        K2 = 0.5 * (self.vx2**2 + self.vy2**2)
        return K1 + K2
    
    @property
    def total_energy(self) -> np.ndarray:
        """
        Total energy = Kinetic energy + potential energy.
        E = K + P.
        """
        return self.kinetic_energy + self.potential_energy

class DoublePendulum(ODEModel):
    """
    Double pendulum with unit masses (M1 = M2 = 1). 
    State ordering: u = [θ1, ω1, θ2, ω2]

    Equations:

        dθ1/dt = ω1
        dθ2/dt = ω2

        dω1/dt =
            L1*ω1^2*sin(Δθ)*cos(Δθ)
          + g*sin(θ2)*cos(Δθ)
          + L2*ω2^2*sin(Δθ)
          - 2*g*sin(θ1)
               2*L1 - L1*cos^2(Δθ)

        dω2/dt =
          - L2*ω2^2*sin(Δθ)*cos(Δθ)
          + 2*g*sin(θ1)*cos(Δθ)
          - 2*L1*ω1^2*sin(Δθ)
          - 2*g*sin(θ2)
               2*L2 - L2*cos^2(Δθ)
    """
    def __init__(self, *, L1: float=1.0, L2: float=1.0, g: float=DEFAULT_G) -> None:
        """
        Parameters:
        L1, L2: float
            Length of  pendulum 1 and 2 in meter. must be >0.
        g: float
            Gravitational acceleration in m/s^2. must be >=0.
        """
        if L1 <= 0 or L2 <= 0: raise ValueError("L1 and L2 must be positive.")
        if g < 0: raise ValueError("g must be positive.")

        self._L1 = float(L1)
        self._L2 = float(L2)
        self._g = float(g)

    @property
    def L1(self) -> float:
        """
            Length of the first pendulum in meter.
            """
        return self._L1

    @property
    def L2(self) -> float:
        """
            Length of the second pendulum in meter.
            """
        return self._L2
        
    @property
    def g(self) -> float:
        """
            Gravitational acceleration (m/s^2).
            """
        return self._g
        
    @property
    def num_states(self) -> int:
        """
            The double pendulum has four state variables.
            """
        return 4
    
    def __call__(self, t: float, u: np.ndarray) -> np.ndarray:
        """
        RHS f(t, u) of the double pendulum ODE.

        Parameters:
        t: float
            Time
        u: np.ndarray
            State vectors containing:
                theta1 = angle of pendulum 1
                omega1 = angular velocity of pendulum 1
                theta2 = angle of pendulum 2
                omega2 = angular velocity of pendulum 2
        
        Returns:
        np.ndarray
            Derivatives: [dθ1/dt, dω1/dt, dθ2/dt, dω2/dt].
        """
        #Unpacking the state variables
        theta1, omega1, theta2, omega2 = u
        #The angle difference
        dtheta = theta2 - theta1

        #Computing the sinus and cosinus values
        sin_dtheta = np.sin(dtheta)
        cos_dtheta = np.cos(dtheta)
        sin_theta1 = np.sin(theta1)
        sin_theta2 = np.sin(theta2)

        #Adding epsilon to avoid division by zero
        eps = 1e-12
        #Denominators in the formulae
        denom1 = (2.0 * self.L1 - self.L1 * cos_dtheta * cos_dtheta) + eps
        denom2 = (2.0 * self.L2 - self.L2 * cos_dtheta * cos_dtheta) + eps

        #Derivate of angels are angular velocity
        dtheta1_dt = omega1
        dtheta2_dt = omega2

        #Equation for angular acceleration og pendelum 1
        # Coupling between pendulums
        # Gravity acting on the pendulums
        # cos and sin terms
        domega1_dt = (
            self.L1 * omega1 * omega1 * sin_dtheta * cos_dtheta
            + self.g * np.sin(theta2) * cos_dtheta
            + self.L2 * omega2 * omega2 * sin_dtheta
            - 2.0 * self.g * sin_theta1
        ) / denom1

        #Equation for angular acceleration of pendelum 2
        # Same as domega1_dt.
        domega2_dt = (
            - self.L2 * omega2 * omega2 * sin_dtheta * cos_dtheta
            + 2.0 * self.g * sin_theta1 * cos_dtheta
            - 2.0 * self.L1 * omega1 * omega1 * sin_dtheta
            - 2.0 * self.g * sin_theta2
        ) / denom2

        #We return an array in the same vector ordering form: [θ1, ω1, θ2, ω2]
        return np.array([dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt], dtype=float)
    
    
    def _create_result(self, solution: Any) -> DoublePendulumResults:
        """
        Adapt SciPy solve_ivp output to our DoublePendulumResults.
        This overrides the parent _create_result method and return 
        DoublePendulumResults object.

        Parameters:
            solution: Any
                The result object from solve_ivp from scipy: time and solution
            
        Returns: 
            DoublePendulumResults: A dataclass holding time, solution and parameters.
        """
        if not hasattr(solution, "t") or not hasattr(solution, "y"):
            raise AttributeError("Solution object must have t and y attributes.")
        #Returning DoublePendulumResults dataclass
        return DoublePendulumResults(
            time=solution.t,
            solution=solution.y,
            L1=self.L1,
            L2=self.L2,
            g=self.g
        )
    
    

def exercise_3d() -> None:
    model = DoublePendulum(L1=1.0, L2=1.0, g=DEFAULT_G)

    #u0 = theta1, omega1, theta2, omega2
    u0 = np.array([np.pi/6, 0.35, 0.0, 0.0], dtype=float)
    T = 10.0
    dt = 0.01

    #Radau used for stiff solver, energy behavior improvement
    result = model.solve(u0=u0, T=T, dt=dt, method="Radau")

    plot_energy(result, filename="energy_double.png")

if __name__ == "__main__":
    exercise_3d()


