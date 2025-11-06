import numpy as np
import labyrinth
from maze_walker import MazeWalker


def test_remove_illegal() -> None:
    """
    @brief This test function, tests the private helper function in MazeWalker that blocks illegal moves.

    @details
    This test uses the example() function giving a small maze from the labyrinth module. A single walker is placed at position (1, 1), which is a legal cell. We then construct all 9 possible 2D moves (stay, 4 cardinal directions, 4 diagonal directions) and pass them to the MazeWalker's private _remove_illegal() method.

    The test verifies that:
    - Any move that would land outside the maze or on a wall (maze[x, y] == False) is replaced by (0, 0), leading to the node staying in still or in place.
    """
    # a 7*7 cross maze is made upon this call.
    maze: np.ndarray = labyrinth.example()
    rng = np.random.default_rng(0)
    # Placing a walker on start position (1,1)
    mw = MazeWalker(1, maze, rng, r0=(1, 1))

    # Trying all the 9 possible moves from start position (1,1).
    steps: np.ndarray = np.array(
        [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 0],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1],
        ]
    )

    # We store the allowed move positions into the ndarray.
    corrected: np.ndarray = mw._remove_illegal(steps.copy())

    # We check that for every step that leads to False in the maze, the corrected step is set to (0,0)
    for i, (dx, dy) in enumerate(steps):
        new_x = mw.x[0] + dx
        new_y = mw.y[0] + dy
        # The different false scenarios we can have
        if (
            new_x < 0
            or new_y < 0
            or new_x >= maze.shape[0]
            or new_y >= maze.shape[1]
            or not maze[new_x, new_y]
        ):
            # We assert to see that the resulting ndarray is correct, for testing purposes
            assert np.all(corrected[i] == np.array([0, 0]))
        else:
            # Legal move is being kept
            assert np.all(corrected[i] == np.array([dx, dy]))
