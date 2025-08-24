import math

def add(x: float, y: float) -> float:
    """Returns the sum of float number x and float number y """
    return x + y

def divide(x: float, y: float) -> float:
    """Returns the dividend of two numbers"""
    return x//y

def factorial(x: int) -> int:
    """Returns n! of input: n"""
    if type(x) != int: 
        raise TypeError("Factorial needs a number as argument")
    if x < 0:
        raise ValueError("Negative not allowed in factorial")
    if x == 0 or x == 1:
        return 1

    val = 1
    for i in range(0, x-1):
        val *= x-i
    return val

def sin(x: float, N=20) -> float:
    """
    Approximate sin(x) using Taylor series with N terms.
    Uses factorial() function above."""
    x = ((x + math.pi) % (2*math.pi)) - math.pi
    sinValue = 0
    for i in range(N + 1):
        sinValue += ((-1)**i) * (x**(2*i + 1)) / factorial(2*i + 1)

    return sinValue
