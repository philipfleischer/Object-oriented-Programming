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
        # self._r0 = r0
        # x0, y0 = r0

        # Checking that the starting square is valid
        if not self._maze[r0[0], r0[1]]:
            raise InvalidSquareError(f"Starting position {r0} is not a legal square.")

        # positions of all walkers; shape (M,x/y)
        # self.x = np.full(M, x0, dtype=int)
        # self.y = np.full(M, y0, dtype=int)
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

    def move(self) -> None:
        """
        @brief This function moves all walkers by one step in 2D.

        Each walker takes one step following the 2D random walk where the trajectory directions are Delta(x), Delta(y) element {-1, 0, 1}
        It updates the positions for the x and y arrays.
        """
        # Drawing the random step components for all the walkers
        dx = self._rng.integers(-1, 2, size=self._M)
        dy = self._rng.integers(-1, 2, size=self._M)

        # Updating the positions
        self._x += dx
        self._y += dy
