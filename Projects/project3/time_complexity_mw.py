import time
import numpy as np
import matplotlib.pyplot as plt
from labyrinth import example
from maze_walker import MazeWalker


def display_maze_walker() -> None:
    """
    @brief This function displays the MazeWalker move()-times for different numbers of walkers on the graph, to analyze the time complexity of the program.

    @details
    For each value of M in a chosen list:
        1. Create the example maze.
        2. Create a MazeWalker(M, maze, rng, r0=(1,1)).
        3. Run N = 1000 calls to move()-function.
        4. Measure total time and divide it by N to get an average time per step.

    The results are plotted:
        X-axis: number of M walkers.
        Y-axis: average time per move() step in seconds.

    @return Plotted display of the graph and a figure called 4a.png.
    """
    maze = example()
    N = 1000
    walker_counts = [10, 50, 100, 200, 500, 1000, 2000]
    avg_times = []

    for M in walker_counts:
        # Instantiating a new pRNG every run, so the sequence is reproducible
        rng_local = np.random.default_rng(1234)
        mw = MazeWalker(M, maze, rng_local, r0=(1, 1))

        start_time = time.perf_counter()  # Start timer before main loop
        for _ in range(N):
            mw.move()  # Performing N steps here
        end_time = time.perf_counter()  # Stop timer

        # Calculating avg time per N step, i.e.: per move()-call
        avg_time = (end_time - start_time) / N
        avg_times.append(avg_time)
        # Print the results in a formatted string style for readability
        print(f"M={M:4d} -> avg time per step = {avg_time:.6e} s")

    # Plotting the results
    plt.figure(figsize=(6, 4))
    plt.plot(walker_counts, avg_times, marker="o")
    plt.title("Time per step vs number of walkers")
    plt.xlabel("Number of walkers M")
    plt.ylabel("Average time per step (in seconds)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("4a.png", dpi=150)  # Figure to png save
    plt.show()


if __name__ == "__main__":
    display_maze_walker()
