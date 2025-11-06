from __future__ import annotations
import numpy as np

from labyrinth import InvalidSquareError


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
        # rng,
        r0: tuple[int, int] = (1, 1),
    ) -> None:
        """
        @param M Number of walkers.
        @param maze 2D boolean array representing the labyrinth.
        @param rng Pseudo-random number generator to use.
        @param r0 Starting position (x0, y0) for all walkers. Defaults to (1, 1).

        @raises InvalidSquareError: if the starting square is not accessible.
        """
        self._M = M
        self._maze = maze
        self._rng = rng
        self._r0 = r0
        x0, y0 = r0

        # Checking that the starting square is valid
        if not self._maze[x0, y0]:
            raise InvalidSquareError(f"Starting position {r0} is not a legal square.")

        # positions of all walkers; shape (M,x/y)
        self.x = np.full(M, x0, dtype=int)
        self.y = np.full(M, y0, dtype=int)

    @property
    def M(self) -> int:
        """@brief Property for number of walkers."""
        return self._M

    @property
    def maze(self) -> np.ndarray:
        """@brief Property for the maze array object."""
        return self._maze

    # move() will be implemented in later tasks
    def move(self) -> None:
        """Placeholder move method to avoid errors occuring in the test_task3a.py file."""
        pass
