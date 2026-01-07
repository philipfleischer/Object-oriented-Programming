import numpy as np
from functools import partial
from timeit import timeit
import numba


# jit = Just In Time. Som betyr:
@numba.jit
def estimate_pi_numba(n: int) -> float:
    sign = np.ones(n)
    # Annenhver. My mer effektivt å gjøre det slik, kontra å bruke løkke
    sign[1::2] = -1
    ivalues = np.arange(n)
    # Denne sum() funksjonen er raskere en python sin egen
    return 4 * np.sum(sign * (1 / (2 * ivalues + 1)))


# njit betyr å operere i noPython mode only
@numba.njit
def estimate_pi_numba_njit(n: int) -> float:
    sign = np.ones(n)
    # Annenhver. My mer effektivt å gjøre det slik, kontra å bruke løkke
    sign[1::2] = -1
    ivalues = np.arange(n)
    # Denne sum() funksjonen er raskere en python sin egen
    return 4 * np.sum(sign * (1 / 2 * ivalues + 1))


if __name__ == "__main__":
    # Må kalle funksjoenne før timeit kjører, så de er ferdig kompilert
    # Hvis vi ikke gjør det får vi ikke en benchmark og ikke en riktig sammenligning
    estimate_pi_numba(1)
    estimate_pi_numba_njit(1)
    for funksjon in [estimate_pi_numba, estimate_pi_numba_njit]:
        n_tester = 1000
        tid = timeit(partial(funksjon, n=100000), number=n_tester)
        print()
        print("Funksjon: ", funksjon.__name__)
        print(f"Tidsbruk: ({n_tester}x: {round(tid, 3)} s)")
