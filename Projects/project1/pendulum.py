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
    
    def plot_energy(self, results: PendulumResults, filename: Optional[str]=None) -> None:
        """
        Plot potential, kinetic and total energy for pendulum solution.

        Parameters:
        results: PendulumResults
            The output we get from the solve() function for pendulums.
        filename: str | None
            If provided, save the figure to the path; else shoe the plot.
        """
        t = results.time
        P = results.potential_energy
        K = results.kinetic_energy
        E = results.total_energy

        plt.figure()
        plt.plot(t, P, label="Potential Energy")
        plt.plot(t, K, label="Kinetic Energy")
        plt.plot(t, E, label="Total Energy", linewidth=2)

        plt.xlabel("Time [s]")      #s: seconds
        plt.ylabel("Energy [J]")    #J: Joule
        plt.title("Pendulum Energy VS. Time")
        plt.grid(True, linestyle="--", alpha=0.4)
        plt.legend()

        if filename:
            plt.savefig(filename, dpi=150, bbox_inches="tight")
            plt.close()
        else:
            plt.show()


def exercise_2b() -> ODEResult:
    """
    Create a Pendulum, solve with u0=[pi/6], T=10, dt=0.01, ans save plot.
    """
    model = Pendulum(L=1.0, g=9.81)

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
    model.plot_energy(result, filename="energy_single.png")


if __name__ == "__main__":
    model = Pendulum(L=1.42, g=9.81)
    u0 = np.array([np.pi/6, 0.35])
    result = model.solve(u0=u0, T=10, dt=0.01)
    print(isinstance(result, PendulumResults))
    exercise_2b()
    exercise_2g()
