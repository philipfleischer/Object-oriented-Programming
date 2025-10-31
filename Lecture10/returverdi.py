from typing import Callable
from numpy import ndarray
from plotspace import plotspace

# NOTE: Kan man da ha en funksjon som 
# returverdi fra en annen funksjon også?

def andregrad(a: float, b: float, c: float) -> Callable[[ndarray], ndarray]:
    """
    Returnerer en funksjon som regner ut f(x) = ax^2 + bx + c.
    """
    def func(x: ndarray) -> ndarray:
        return a*x**2 + b*x + c
    return func

if __name__ == "__main__":
    h = andregrad(a=1, b=2, c=3)
    print(h(-1))
    print(h(0))
    print(h(1))
    plotspace(h, -10, 10, 100)