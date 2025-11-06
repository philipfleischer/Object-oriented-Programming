import matplotlib.pyplot as plt
import matplotlib.figure
import matplotlib.collections
from typing import Protocol
import numpy as np

from matplotlib.animation import FuncAnimation

try:
    from .labyrinth import plot
except ImportError:
    from labyrinth import plot


class MazeWalker(Protocol):
    x: np.ndarray
    y: np.ndarray
    maze: np.ndarray

    def move(self) -> None: ...


class Animation:
    """Class for animating maze walkers."""

    def __init__(self, mw: MazeWalker, color: str = "springgreen"):
        """
        Parameters
        ----------
        mw : MazeWalker
            A MazeWalker instance
        color : str, optional
            A string representing the color of the walkers,
            by default "springgreen". See
            https://matplotlib.org/stable/gallery/color/named_colors.html
            for a full list of colors
        """
        self._mw = mw
        self.color = color

    def plot(self, size: int, show: bool = True) -> matplotlib.figure.Figure:
        """Figure containing the labyrinth and the walkers.

        Parameters
        ----------
        size : int
            Size of the dots representing the walkers
        show : bool, optional
            If True show the plot directly, otherwise just return
            the figure, by default True

        Returns
        -------
        matplotlib.figure.Figure
            The figure
        """
        fig, ax = plt.subplots()
        plot(self._mw.maze)
        self._pos = ax.scatter(
            self._mw.x,
            self._mw.y,
            c=self.color,
            s=size,
            alpha=0.4,
        )
        ax.set_title("Frame 0")
        if show:
            plt.show()
        return fig

    def _update_frame(self, i: int) -> tuple[matplotlib.collections.PathCollection]:
        """Method for updating the animation

        Parameters
        ----------
        i : int
            The index of the frame

        Returns
        -------
        tuple[matplotlib.collections.PathCollection]
            Object containing the dots
        """
        self._mw.move()
        self._pos.set_offsets(np.array([self._mw.x, self._mw.y]).T)
        self._pos.axes.title.set_text(f"Frame {i}")
        return (self._pos,)

    def animate(
        self,
        N: int,
        size: int = 10,
        interval: int = 1,
        filename: str = "",
        show: bool = True,
    ) -> FuncAnimation:
        """Animate random walk in maze

        Parameters
        ----------
        N : int
            Number of frames
        size : int, optional
            Size of the dots representing the walkers, by default 10
        interval : int, optional
            Delay between frames in milliseconds, by default 1
        filename : str, optional
            Filename to save the animation, by default ""
        show : bool, optional
            If True show the animation, by default True

        Returns
        -------
        FuncAnimation
            Animation object
        """
        fig = self.plot(size, show=False)
        animation = FuncAnimation(
            fig,
            self._update_frame,
            interval=interval,
            repeat=False,
            frames=N,
        )
        if filename != "":
            animation.save(filename)
        if show:
            plt.show()
        return animation
