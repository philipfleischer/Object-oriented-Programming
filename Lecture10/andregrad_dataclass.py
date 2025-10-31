from dataclasses import dataclass
from math import pi

@dataclass
class AndregradsPolynom:
    a: int | float=1
    b: int | float=0
    c: int | float=0

    def __str__(self) -> str:
        """Runder av koeffesientene til 2 desimaler"""
        return f"AndregradsPolynom( a = {round(self.a, 2)}, " \
                                    + f"b = {round(self.b, 2)}, " \
                                    + f"c = {round(self.c, 2)} )"
    

if __name__ == "__main__":
    test = AndregradsPolynom(pi, pi, pi)
    print(test)

    test.b = 1
    test.c = -1
    print(test)