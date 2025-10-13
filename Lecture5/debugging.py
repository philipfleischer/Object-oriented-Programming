def div(x: int | float, y: int | float) -> float:
    return x / y

def sub(x: int | float, n: int) -> int | float:
    return x-n

def solve(x: int | float, y: int | float) -> int | float:
    y2 = sub(y, 1)
    return div(x, y2)

for i in range(100, 0, -1):
    solve(i, i-1)