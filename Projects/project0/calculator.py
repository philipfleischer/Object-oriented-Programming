import math

def add(x: float, y: float) -> float:
    """Returns the sum of float number x and float number y """
    return x + y

def divide(x: float, y: float) -> float:
    """Returns the divided result of two float values.
    Raises ZeroDivisionError if detected"""
    return x/y

def factorial(x: int) -> int:
    """Returns n! of input: n, for non-negative integers.
    Raises Typerror and ValueError if it detects it."""
    if not isinstance(x, int): 
        raise TypeError("Factorial needs a number as argument")
    if x < 0:
        raise ValueError("Negative not allowed in factorial")

    val = 1
    for i in range(0, x-1):
        val *= x-i
    return val

def sin(x: float, N=20) -> float:
    """
    Approximate sin(x) using Taylor series with N terms.
    Uses factorial() function above.
    N should be small (e.g.: N=20)"""
    x = ((x + math.pi) % (2*math.pi)) - math.pi
    sin_value = 0
    for i in range(N + 1):
        sin_value += ((-1)**i) * (x**(2*i + 1)) / factorial(2*i + 1)

    return sin_value
