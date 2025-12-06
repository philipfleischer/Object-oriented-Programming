from functools import partial
from timeit import timeit

from pi_mypyc import estimate_pi


def estimate_pi_local(n: int) -> float:
    """Estimerer pi med Leibniz formel (fra taylor-rekker)."""
    pi_delt_pa_4 = 0.0
    for i in range(n):
        pi_delt_pa_4 += (-1.0) ** i / (2.0 * i + 1.0)
    return 4 * pi_delt_pa_4


if __name__ == "__main__":
    for funksjon in [estimate_pi, estimate_pi_local]:
        n_tester = 1000
        tid = timeit(partial(funksjon, n=100000), number=n_tester)
        print()
        print("Funksjon: ", funksjon.__name__)
        print(f"Tidsbruk: ({n_tester}x: {round(tid, 3)} s)")
