from numpy.random import randint
import matplotlib.pyplot as plt


class DrunkWalker:
    """Simulerer en full person som vandrer hjem (1D)."""

    def __init__(self, home: int) -> None:
        """Oppretter en ny vandrer i x=0 med x=home som hjemsted."""
        self._x = 0  # Posisjon
        self._home = home
        self._history = [0]

    @property
    def position(self) -> int:
        return self._x

    @property
    def nsteps(self) -> int:
        """Antall steg vandreren har gått til nå."""
        return len(self._history)

    @property
    def is_at_home(self) -> bool:
        """True hvis vandreren er hjemme, ellers False."""
        return self.position == self._home

    def step(self) -> None:
        """Vandreren tar et steg i +/- retning (tilfeldig)."""
        self._x += 2 * randint(2) - 1
        self._history.append(self._x)

    def walk_home(self) -> int:
        """Går tilfeldige steg helt til hjemme. Returnerer antall steg brukt."""
        while not self.is_at_home:
            self.step()
        return self.nsteps

    def plot(self) -> None:
        """Plotter alel posisjoner vandreren har vært innom til nå."""
        plt.plot(range(self.nsteps), self._history, alpha=0.7)


def main(nwalkers: int) -> None:
    """Eksempelkode for DrunkWalker med n objekter og 100 som hjem."""
    for _ in range(nwalkers):
        drunkard = DrunkWalker(100)
        drunkard.walk_home()
        drunkard.plot()
    plt.show()


if __name__ == "__main__":
    main(5)
