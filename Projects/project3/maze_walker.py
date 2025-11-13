from __future__ import annotations
import matplotlib.pyplot as plt
import numpy as np
from labyrinth import (
    InvalidSquareError,
    circular,
    example,
    layered_labyrinth,
    get_legal_line,
    plot,
)
from animation import Animation
import pstats


class MazeWalker:
    """
    @brief The MazeWalker class represents M random walkers inside a 2D maze.

    The class stores the maze (a boolean 2D array), the number of walkers, a random number generator, and the current positions of all the walkers.
    All walkers start at the same initial position r0=(x0,y0), unless another starting point is explicitly set.
    """

    def __init__(
        self,
        M: int,
        maze: np.ndarray,
        rng: np.random.Generator,
        r0: tuple[int, int] = (1, 1),
        endpoints: list[tuple[int, int]] | None = None,
    ) -> None:
        """
        @param M Number of walkers.
        @param maze 2D boolean array representing the labyrinth.
        @param rng Pseudo-random number generator to use.
        @param r0 Starting position (x0, y0) for all walkers. Defaults to (1, 1).
        @param endpoints List of coordinates that are endpoints in the maze.

        @raises InvalidSquareError: if the starting square is not accessible.
        """
        self._M = M
        self._maze = maze
        self._rng = rng
        # if endpoints list is not given, we initialize it as an empty list.
        self._endpoints = endpoints or []

        # Checking that the starting square is valid
        if not self._maze[r0[0], r0[1]]:
            raise InvalidSquareError(f"Starting position {r0} is not a legal square.")

        self.initialize_walkers(r0)

    @property
    def M(self) -> int:
        """@brief Property for number of walkers."""
        return self._M

    @property
    def maze(self) -> np.ndarray:
        """@brief Property for the maze array object."""
        return self._maze

    def initialize_walkers(self, r0: tuple[int, int]) -> None:
        """
        @brief This function initializes all walkers at the start position r0=(x0,y0).

        @param r0 This is a tuple of integers (x0,y0) representing the starting position.

        @raises InvalidSquareError If the start position is not valid.
        """
        x0, y0 = r0
        if not self._maze[x0, y0]:
            raise InvalidSquareError(f"Starting position {r0} is not a legal square.")

        self._x = np.full(self._M, x0, dtype=int)
        self._y = np.full(self._M, y0, dtype=int)

    @property
    def x(self) -> np.ndarray:
        """@brief X-position of all walkers."""
        return self._x

    @property
    def y(self) -> np.ndarray:
        """@brief Y-position of all walkers."""
        return self._y

    def _remove_illegal(self, dr: np.ndarray) -> np.ndarray:
        """
        @brief This function filters out steps that would move walkers into walls or outside of the maze.

        @details
        This helper function checks each proposed step (Δx, Δy) in the dr array      and replaces any non-valid steps with (0, 0).
        A step is considered illegal if it moves a walker:
          - Outside the maze boundary, or
          - Into a wall: a cell where maze[x, y] == False.

        The function supports both:
          - The standard case (K == M): one proposed step per walker, and
          - The testing case (K != M): multiple trial steps from a single position.

        @param dr Array of shape (K, 2), where each row is a proposed (Δx, Δy) step.

        @return Array of shape (K, 2) where illegal steps have been replaced by (0, 0).
        """
        # Number of rows and columns in the maze.
        nrows, ncols = self._maze.shape
        # The number of proposed steps to take.
        K = dr.shape[0]

        # This is the case for when it is one proposed step per walker
        if K == self._M:
            cur_x = self._x
            cur_y = self._y
        else:
            # Testing case: use position of first walker for all proposed steps
            cur_x = np.full(K, self._x[0], dtype=int)
            cur_y = np.full(K, self._y[0], dtype=int)

        # This is the proposed new positions to be computed
        new_x = cur_x + dr[:, 0]
        new_y = cur_y + dr[:, 1]

        # Initialize all moves to be legal, then update
        legal = np.ones(K, dtype=bool)

        # Checking to see if moves is inside bounds?
        inside_x = (new_x >= 0) & (new_x < nrows)
        inside_y = (new_y >= 0) & (new_y < ncols)
        inside = inside_x & inside_y

        # Keep only those that are inside (bitwise AND operator)
        legal = legal & inside

        # For the positions that are valid, we check they also land on True (open pathway cell).
        legal[inside] &= self._maze[new_x[inside], new_y[inside]]

        # Identifying illegal moves (legal==False)
        illegal = np.logical_not(legal)
        # Replacing all illegal steps with (0,0)
        dr[illegal, :] = 0

        return dr

    def not_finished(self) -> np.ndarray:
        """
        @brief Return a boolean array of walkers that may still move. A walker is finished if it is currently standing on one of the endpoint coordinates. Finished walkers get bool False, others get True.

        @return np.ndarray object with shape (M, ).
        """
        movable_walkers = np.ones(self._M, dtype=bool)
        if not self._endpoints:
            # No endpoints defined -> everyone can move
            return movable_walkers

        # For each endpoint, mark walkers that are there as finished.
        for x_endpoint, y_endpoint in self._endpoints:
            at_endpoint = (self._x == x_endpoint) & (self._y == y_endpoint)
            movable_walkers[at_endpoint] = False

        return movable_walkers

    def move(self) -> None:
        """
        @brief This function moves all walkers by one random step in 2D.

        @details
        Each walker takes one step following the 2D random walk where the trajectory directions are Delta(x), Delta(y) element {-1, 0, 1}
        Before it updates the positions for the x and y arrays, illegal steps are replaced with (0,0) using the _remove_illegal_moves() method.
        """
        # Drawing the random step components for all the walkers
        dx = self._rng.integers(-1, 2, size=self._M)
        dy = self._rng.integers(-1, 2, size=self._M)

        # Stacking (dx, dy) into array for proposed next steps.
        dr = np.stack((dx, dy), axis=1)
        # removing and replacing illegal moves before updating the walkers.
        dr = self._remove_illegal(dr)

        # Figuring out which wealkers are still allowed to move
        movable_walkers = self.not_finished()

        # Updating all the walker positions
        self._x[movable_walkers] += dr[movable_walkers, 0]
        self._y[movable_walkers] += dr[movable_walkers, 1]


if __name__ == "__main__":
    rng = np.random.default_rng(1234)

    # Constructing the circular maze
    maze = circular()

    # Making the maze walker with 500 walkers and start position (100, 100).
    maze_walk_inst = MazeWalker(
        M=500,
        maze=maze,
        rng=rng,
        r0=(100, 100),
        endpoints=[],
    )

    # Animating the maze walker with 200 time steps.
    animate = Animation(maze_walk_inst)
    animate.animate(N=200, size=10, interval=30)

    # Running the debugging tip here:
    maze = example()
    walker = MazeWalker(M=1, maze=maze, rng=rng, r0=(1, 1), endpoints=[(5, 5)])
    animation = Animation(walker)
    animation.animate(N=100, interval=200, size=200)

    # Task 4b:
    p = pstats.Stats("maze.cprof")
    p.sort_stats("cumtime").print_stats(20)

    # Task 3h:
    maze = layered_labyrinth(layers=2)

    fig, ax = plt.subplots(figsize=(8, 6))
    plot(maze, ax=ax)

    line = maze.shape[1] - 2
    start_points = get_legal_line(maze, y=line)
    endpoints = get_legal_line(maze, y=1)

    ax.plot(*zip(*start_points), "go")
    ax.plot(*zip(*endpoints), "r.")
    plt.show()  

    # Choose a starting point
    r0 = start_points[len(start_points) // 2]

    M = 100_000
    walker = MazeWalker(M=M, maze=maze, rng=rng, r0=r0, endpoints=endpoints)

    anim = Animation(walker)
    anim.animate(N=2000, interval=1, size=5)

    # Find walkers that reached an endpoint
    finished_mask = ~walker.not_finished()
    finished_x = walker.x[finished_mask]
    print("Number of walkers that reached an endpoint:", finished_x.size)

    # Histogram of x-positions at endpoints
    plt.figure()
    plt.hist(
        finished_x,
        bins=maze.shape[0],
        range=(0, maze.shape[0]),
    )
    plt.xlabel("x-position at endpoint")
    plt.ylabel("Number of walkers")
    plt.title("Task 3h: x-positions of walkers at endpoints")
    plt.savefig("3h.png", dpi=150, bbox_inches="tight")
    plt.close()

