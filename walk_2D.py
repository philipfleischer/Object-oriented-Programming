import numpy as np
import matplotlib.pyplot as plt

seed = 1234
rng = np.random.default_rng(seed)


def walker2D():
    """
    @brief This function simulates and plots a 2D random walker.

    The walker starts at position (0, 0) and takes N = 50 steps. At each step the x- and y-components of the step are chosen independently from {-1, 0, 1} with equal probability. This means the walker can move horizontally, vertically, diagonally, or stand still.

    The function plots the trajectory in the xy-plane and marks the start- and end-points.

    @returns None
    Displays a plot figure showing the 2D random walk.
    """
    num_steps = 50

    # Storing positions in x and y arrays
    x = np.zeros(num_steps + 1)
    y = np.zeros(num_steps + 1)

    # Generating random steps in x and y
    dx = rng.integers(low=-1, high=2, size=num_steps)
    dy = rng.integers(low=-1, high=2, size=num_steps)

    # Using the cumulative function on the positions in the arrays usign the randomly generated steps
    x[1:] = np.cumsum(dx)
    y[1:] = np.cumsum(dy)

    # Ploting the path
    plt.plot(
        x, y, color="blue"
    )  # Should i use "tab:blue" or something for better visuals maybe?
    # Marking the start- and end-points in the plot
    plt.scatter([0], [0], color="green", label="start")
    plt.scatter([x[-1]], [y[-1]], color="red", label="end")

    # Setting up the plot details
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("2D random walk (1 walker, N=50)")
    plt.legend()
    # Using this, so that the steps look square
    plt.axis("equal")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    walker2D()
