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


def walker1D():
    seed = 1234
    rng = np.random.default_rng(seed)

    N = 50
    Xs = np.zeros(N + 1)
    ns = np.arange(N + 1)
    dxs = rng.integers(low=-1, high=2, size=N)
    Xs[1:] = np.cumsum(dxs)

    plt.step(ns, Xs, color="blue")
    plt.xlabel(r"Step number $n$")
    plt.ylabel(r"Position $x_n$")
    plt.title("1D random walk (1 walker, N=50)")
    plt.show()


if __name__ == "__main__":
    walker1D()
