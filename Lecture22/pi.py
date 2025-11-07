from functools import partial
from time import perf_counter
from timeit import timeit
from matplotlib.bezier import inside_circle
import numpy as np


def monte_carlo_pi(N: int) -> float:
    inside_circle = 0
    # Kvadrat med areal 4, hvor både x og y er mellom -1 og 1
    for _ in range(N):
        x = 2 * np.random.random() - 1
        y = 2 * np.random.random() - 1
        # Er dette tilfeldige punktet innenfor sirkelen?
        r2 = x**2 + y**2
        if r2 <= 1:
            inside_circle += 1
    # pi = areal av sirkel = andel av sirkel * areal av kvadrat
    return (inside_circle / N) * 4


def pi_libniz(N: int) -> float:
    """Estimerer pi med Leibniz' formel (fra Taylor-rekker)"""
    pi_delt_på_4 = 0.0
    for i in range(N):
        pi_delt_på_4 += (-1.0) ** i / (2.0 * i + 1.0)
    return 4 * pi_delt_på_4


def pi_numpy(N: int) -> float:
    """Som pi_leibniz, men bruker numpy (vektorisert) i stedet for løkke"""
    fortegn = np.ones(N)
    # Bytter fortegn for annenhvert element
    fortegn[1::2] = -1
    ivalues = np.arange(N)
    return 4 * np.sum(fortegn * (1 / (2 * ivalues + 1)))


if __name__ == "__main__":
    N = 1000

    # Timer
    for funksjon in [monte_carlo_pi, pi_libniz, pi_numpy]:
        pi_N = funksjon(N)
        tid = timeit(partial(funksjon, N=N), number=1000)
        print()
        print(funksjon.__name__)
        print("pi: ", pi_N)
        print("Tidsbruk (1000x): ", round(tid, 3), "s")
    print()
