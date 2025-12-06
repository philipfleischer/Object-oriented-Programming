import numpy as np
import matplotlib.pyplot as plt

seed = 1234
rng = np.random.default_rng(seed)


def walker2D() -> None:
    """
    @brief This function simulates and plots a 2D random walker.

    The walker starts at position (0, 0) and takes N = 50 steps. At each step the x- and y-components of the step are chosen independently from {-1, 0, 1} with equal probability. This means the walker can move horizontally, vertically, diagonally, or stand still.

    The function plots the trajectory in the xy-plane and marks the start- and end-points.

    @returns None
    Displays a plot figure showing the 2D random walk.
    """
    num_steps = 500

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
    # Using this for accurate visual representation purposes
    plt.axis("equal")
    plt.grid(True)
    plt.show()


def many_walkers_2D() -> None:
    """
    @brief This function simulates and plots multiple 2D random walkers.

    It simulates M=5 walkers taking N=500 steps in 2D. Each walker starts at position (0, 0). At every time step, Δx and Δy are chosen
    independently from the set of: {-1, 0, +1}, with an equal probability.

    All five walker trajectories are plotted in the same figure with unique colors. The figure displays the displacement: y versus x.

    @returns None
    Displays a plotted figure with all 5 walker trajectories.
    """
    num_steps = 500
    num_walkers = 5

    # Initialized some colors to use
    colors = ["blue", "red", "green", "orange", "purple"]

    plt.figure(figsize=(6, 6))

    for i in range(num_walkers):
        # Generating the random steps
        dx = rng.integers(low=-1, high=2, size=num_steps)
        dy = rng.integers(low=-1, high=2, size=num_steps)

        x = np.zeros(num_steps + 1)
        y = np.zeros(num_steps + 1)
        x[1:] = np.cumsum(dx)
        y[1:] = np.cumsum(dy)

        # Plotting each individual walker
        plt.plot(x, y, color=colors[i], label=f"Walker {i+1}")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("2D random walk (5 walkers, N=500)")
    plt.legend()
    plt.axis("equal")
    plt.grid(True)
    plt.show()


def simulate_2d_walkers(
    num_steps: int, num_walkers: int, rng: np.random.Generator
) -> np.ndarray:
    """
    @brief This function simulates 2D random walks for many walkers.

    Each walker starts at position (0,0) and at every step moves by (Δx, Δy), where Δx, Δy are chosen independently from {-1, 0, +1} with equal probability.

    @param num_steps Number of time steps N.
    @param num_walkers Number of walkers M.
    @param rng NumPy random Generator instance.

    @return positions of array of shape (num_steps+1, num_walkers, 2) where positions[n, m] = (x_n, y_n) for walker m at time n.
    """
    # Shape format: (num_steps, num_walkers, 2)
    dx = rng.integers(low=-1, high=2, size=(num_steps, num_walkers))
    dy = rng.integers(low=-1, high=2, size=(num_steps, num_walkers))

    positions = np.zeros((num_steps + 1, num_walkers, 2))
    # Cumulative sum over the time (axis=0)
    positions[1:, :, 0] = np.cumsum(dx, axis=0)  # x-array
    positions[1:, :, 1] = np.cumsum(dy, axis=0)  # y-array

    # Returning current position
    return positions


def plot_positions_at_final_time(positions: np.ndarray, final_step: int) -> None:
    """
    @brief This function scatters the plot to all walker positions at a given time.

    @param positions Array of shape (num_steps+1, M, 2).
    @param final_step Time index to be plotted (e.g. 500).
    """
    xy = positions[final_step]
    x_final = xy[:, 0]
    y_final = xy[:, 1]

    plt.figure(figsize=(6, 6))
    plt.scatter(x_final, y_final, s=10, alpha=0.6)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"2D random walk: positions at step n={final_step}")
    plt.axis("equal")
    plt.grid(True)
    plt.show()


def plot_rms_vs_time(positions: np.ndarray) -> None:
    """
    @brief This function plots the RMS as a function of time for different sample sizes, together with the analytical RMS.

    It uses M=10,100,1000.

    @param positions Array of shape (num_steps+1, M, 2) with M >= 1000.
    """
    num_steps = positions.shape[0] - 1
    step_indices = np.arange(num_steps + 1)

    # analytical RMS in 2D: sqrt( <x_n^2> + <y_n^2> ) = sqrt(4/3 * n)
    analytical_rms = np.sqrt((4.0 / 3.0) * step_indices)

    plt.figure(figsize=(7, 5))

    for M in [10, 100, 1000]:
        # slice first M walkers
        pos_M = positions[:, :M, :]  # (N+1, M, 2)
        # squared distance from origin for each walker, each time
        r2 = pos_M[:, :, 0] ** 2 + pos_M[:, :, 1] ** 2  # (N+1, M)
        # mean over walkers
        mean_r2 = np.mean(r2, axis=1)  # (N+1,)
        rms = np.sqrt(mean_r2)
        plt.plot(step_indices, rms, label=f"Simulated M={M}")

    # plot analytical
    plt.plot(step_indices, analytical_rms, "k--", label="Analytical RMS = √(4n/3)")

    plt.xlabel("Step number n")
    plt.ylabel("RMS distance")
    plt.title("RMS of 2D random walk vs time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    walker2D()
    many_walkers_2D()

    N = 500
    M = 1000
    positions = simulate_2d_walkers(N, M, rng)
    plot_positions_at_final_time(positions, final_step=500)
    plot_rms_vs_time(positions)
