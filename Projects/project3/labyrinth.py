from __future__ import annotations
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.axes
import matplotlib.image


class InvalidSquareError(LookupError):
    pass


def get_legal_line(maze: np.ndarray, y: int) -> list[tuple[int, int]]:
    """All legal points at a certain line of maze

    Parameters
    ----------
    maze : np.ndarray
        The array representing the maze
    y : int
        Coordinte for the line

    Returns
    -------
    list[tuple[int, int]]
        List of points that are valid along this line

    Raises
    ------
    TypeError
        If `y` is not an integer
    """
    if not isinstance(y, (int, np.integer)):
        raise TypeError("line number y must be an int.")
    return [(x[0], y) for x in np.argwhere(maze[:, y])]


def plot(
    maze: np.ndarray, ax: matplotlib.axes.Axes | None = None
) -> matplotlib.image.AxesImage:
    _ax = ax or plt.gca()
    im = _ax.imshow(maze.T, origin="lower", cmap="gray")
    im.set_clim(vmax=1)
    _ax.set_axis_off()
    return im


def circular(R: int = 100, padding: int = 2) -> np.ndarray:
    """Create a circular area.

    Parameters
    ----------
    R : int, optional
        radius of the circular area, by default 100
    padding : int, optional
        padding around the area, by default 2

    Returns
    -------
    np.ndarray
       Boolean array with True inside the circle and False outside
    """
    N = int(2 * (R + padding) + 1)
    c = (N - 1) // 2
    x = np.arange(N)
    xx, yy = np.meshgrid(x, x)
    return (xx - c) ** 2 + (yy - c) ** 2 <= R**2


def example() -> np.ndarray:
    """Create an example labyrinth

    Returns
    -------
    np.ndarray
       Boolean array with True inside the labyrinth and False outside
    """
    arr = np.zeros((7, 7), dtype=bool)
    indices = np.array([1, 3, 5])
    arr[1:-1, indices] = True
    arr[indices, 1:-1] = True
    return arr


def layered_labyrinth(layers: int = 2, width: int = 3, height: int = 5) -> np.ndarray:
    """Create a layered labyrinth

    Parameters
    ----------
    layers : int, optional
        Number of layers, by default 2
    width : int, optional
        The width of the labyrinth, by default 3
    height : int, optional
        The height of the labyrinth, by default 5

    Returns
    -------
    np.ndarray
        Boolean array with True inside the labyrinth and False outside
    """
    bars = 3 ** (layers + 1)
    Mx = 2 + width * bars + bars - 1
    My = 2 + height * (layers + 2) + width * (layers + 1)
    arr = np.zeros((Mx, My), dtype=bool)
    jump = 4
    for n in range(layers + 2):
        start0 = 2 * 3**n - 1
        start1 = n * (height + width) + 1
        end1 = start1 + height
        for j in range(width):
            arr[start0 + j :: jump, start1:end1] = True
        if n != layers + 1:
            arr[start0:-start0, end1 : end1 + width] = True
        jump *= 3
    return arr
