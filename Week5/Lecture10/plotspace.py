from numpy import linspace, ndarray
import matplotlib.pyplot as plt
from andregrad_namedtuple import AndregradsPolynom
from typing import Callable

#NOTE: Kan faktisk ha en funksjon som parameter til en anenn funksjon
def plotspace(f: Callable[[ndarray], ndarray], 
              min: float,
              max: float,
              n: int) -> None:
    """
    min, max, n akkurat som linspace fra numpy.
    Plotter f(x der x er en array som lages med linspace)
    """

    x =linspace(min, max, n)
    y = f(x)

    plt.plot(x,y)
    plt.title("$" + str(f) + "$") #Alt mellom $$ blir LaTex-formatert
    plt.show()

if __name__ == "__main__":
    for a in range(2):
        for b in range(2):
            for c in range(3):
                g = AndregradsPolynom(a, b, c)
                # NOTE: Kaller nå funksjon med annen "funksjon" som argrumet
                plotspace(g, -10, 10, 100)