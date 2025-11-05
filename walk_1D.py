import numpy as np
import matplotlib.pyplot as plt

# Global RNG and seed so all functions use the same generator and seed.
seed = 1234
rng = np.random.default_rng(seed)


def walker1D():
    """
    @brief The walker1D() function initializes and plots a one-dimensional random walker. This function performs a stochastic simulation of a single random walker in one dimension. The walker starts at position x_0 = 0 and takes N = 50 steps. the walker can move move left, right, or remain still.

    @details
    The function uses NumPy's pseudo-random number generator to ensure reproducibility and Matplotlib to visualize the random walk.

    @note The random number generator seed is fixed to 1234 for reproducibility and consistent outputs.

    @returns None
    Displays a Matplotlib plot showing the 1D random walk trajectory.
    """
    num_steps = 50
    positions = np.zeros(num_steps + 1)
    step_indices = np.arange(num_steps + 1)

    steps = rng.integers(low=-1, high=2, size=num_steps)
    positions[1:] = np.cumsum(steps)

    plt.step(step_indices, positions, color="blue")
    plt.xlabel(r"Step number $n$")
    plt.ylabel(r"Position $x_n$")
    plt.title("1D random walk (1 walker, N=50)")
    plt.show()


def many_walkers_1D():
    """
    @brief This function simulates and plot many 1D random walkers.
    Using M = 1000 walkers and N = 500 time steps. All trajectories are plotted in the same figure with the use of transparency.
    """
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

    # Returning to use displacement visualized plot
    return positions, num_steps


def compare_walkers_to_analytic(positions, num_steps):
    """
    @brief This function compares simulated random-walk statistics to analytical results.
    It computes the mean displacement and RMS from the simulated random walk data for values of M = 10, 100, and 1000 walkers, and compares them with the analytical expectations.

    @param positions 2D array of shape (num_steps+1, num_walkers).
    @param num_steps Number of time steps.

    @returns None
    It displays a plot figure with two side-by-side plots.
    """
    step_indices = np.arange(num_steps + 1)

    # Analytical expression values to be used in plot
    analytical_mean = np.zeros(num_steps + 1)
    analytical_rms = np.sqrt((2 / 3) * step_indices)

    # Using the subplot function to display them side-by-side upon plotting
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # M is the number of walkers
    for M in [10, 100, 1000]:
        sliced_positions = positions[:, :M]
        mean_displacement = np.mean(sliced_positions, axis=1)
        rms = np.sqrt(np.mean(sliced_positions**2, axis=1))

        axes[0].plot(step_indices, mean_displacement, label=f"M={M}")
        axes[1].plot(step_indices, rms, label=f"M={M}")

    # Plotting and adding the analytical curves to the plots
    axes[0].plot(step_indices, analytical_mean, "k--", label="Analytical ⟨xₙ⟩ = 0")
    axes[1].plot(step_indices, analytical_rms, "k--", label="Analytical RMS = √(2n/3)")

    # Setting the plots up
    axes[0].set_title("Mean displacement ⟨xₙ⟩ vs. steps")
    axes[0].set_xlabel("Step number (n)")
    axes[0].set_ylabel("Mean displacement ⟨xₙ⟩")
    axes[0].legend()

    axes[1].set_title("Root mean square displacement RMS(xₙ) vs. steps")
    axes[1].set_xlabel("Step number (n)")
    axes[1].set_ylabel("RMS displacement")
    axes[1].legend()

    # Using this to avoid overlap
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    walker1D()
    pos, nums = many_walkers_1D()
    compare_walkers_to_analytic(pos, nums)
