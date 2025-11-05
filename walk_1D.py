import numpy as np
import matplotlib.pyplot as plt

"""
@brief The walker1D() function initializes and plots a one-dimensional random walker. This function performs a stochastic simulation of a single random walker in one dimension. The walker starts at position x_0 = 0 and takes N = 50 steps. the walker can move move left, right, or remain still.

@details
The function uses NumPy's pseudo-random number generator to ensure reproducibility and Matplotlib to visualize the random walk.

@note The random number generator seed is fixed to 1916 for reproducibility and consistent outputs.

@returns None
Displays a Matplotlib plot showing the 1D random walk trajectory.
"""
seed = 1234
rng = np.random.default_rng(seed)


def walker1D():
    num_steps = 50
    posisions = np.zeros(num_steps + 1)
    step_indices = np.arange(num_steps + 1)
    steps = rng.integers(low=-1, high=2, size=num_steps)
    posisions[1:] = np.cumsum(steps)

    plt.step(step_indices, posisions, color="blue")
    plt.xlabel(r"Step number $n$")
    plt.ylabel(r"Position $x_n$")
    plt.title("1D random walk (1 walker, N=50)")
    plt.show()


"""
@brief This functions simulates and plot many 1D random walkers.
Using M = 1000 walkers and N = 500 time steps. All trajectories are plotted in the same figure with the use of transparency.
"""


def many_walkers_1D():
    num_steps = 500
    num_walkers = 1000
    positions = np.zeros((num_steps + 1, num_walkers))
    step_indices = np.arange(num_steps + 1)
    steps = rng.integers(low=-1, high=2, size=(num_steps, num_walkers))
    positions[1:, :] = np.cumsum(steps, axis=0)

    for walker_idx in range(num_walkers):
        plt.plot(step_indices, positions[:, walker_idx], color="blue", alpha=0.02)

    plt.xlabel(r"Step number $n$")
    plt.ylabel(r"Position $x_n$")
    plt.title(f"1D random walk ({num_walkers} walkers, N={num_steps})")
    plt.show()


if __name__ == "__main__":
    walker1D()
    many_walkers_1D()
