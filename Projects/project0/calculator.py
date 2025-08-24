def add(x: float, y: float) -> float:
    """Returns the sum of float number x and float number y """
    return x + y

def divide(x: float, y: float) -> float:
    """Returns the dividend of two numbers"""
    return x//y

def factorial(x: int) -> int:
    """Returns n! of input: n"""
    val = x
    for i in range(0, x-1):
        val *= x-i
    return val

def sin(x: int, N: 20) -> int:
    pass
