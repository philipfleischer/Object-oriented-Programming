from numpy import ndarray
from typing import NamedTuple

class AndregradsPolynom(NamedTuple):
    """Klasse som representerer et andregradpolynom: a*x**2 + b*x + c"""
    a: float | int=1
    b: float | int=0
    c: float | int=0

    #Som i en dataclass, kan vi ha vanlige metoder ogsp i en NamedTuple
    def __str__(self) -> str:
        """Runder av koeffisientene til 2 desimaler"""
        utrskrift = ""
        if self.a != 1:
            utrskrift += str(round(self.a, 2))
        utrskrift += "x^2"

        if self.b != 0:
            utrskrift += " + "
            if self.b != 1:
                utrskrift += str(round(self.b, 2))
            utrskrift += "x"

        if self.c != 0:
            utrskrift += " + "
            utrskrift += str(round(self.c))

        return utrskrift
    
    def __call__(self, x: ndarray) -> ndarray:
        return self.a*x**2 + self.b*x + self.c

if __name__ == "__main__":
    test = AndregradsPolynom()
    print(test)

    test2 = AndregradsPolynom(2,0,1)
    print(test2)