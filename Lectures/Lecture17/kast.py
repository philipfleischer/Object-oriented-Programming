from random import randint
from httpcore import NetworkStream
import numpy as np
import numpy.random as npr
from functools import partial
from timeit import timeit
from matplotlib import pyplot as plt

for i in range(3):
    kast = randint(0, 1)  # Fra og med 0, til og med 1
    if kast == 1:
        print("Mynt")
    else:
        print("Krone")


def ett_og_ett_kast(nkast: int) -> tuple[int]:
    nmynt = 0
    for _ in range(nkast):
        kast = randint(0, 1)
        if kast == 1:
            nmynt += 1
    nkrone = nkast - nmynt
    return nmynt, nkrone  # Pakker feler returverdier inn i en tuple


def vektoriserte_kast(nkast: int) -> tuple[int]:
    # Note: Tilsaverer random.randint(0,1)
    #   numpy: fra OG med 0, til (IKKE MED) 2
    kast = npr.randint(0, 2, size=nkast)
    # Kast er nå en array med verdier 0 eller 1, f.eks: [0 1 1 0 0 1 1 0 1 ...]
    nmynt = np.sum(kast)  # NOTE: np.sum() og ikke sum() for hastighet
    nkrone = nkast - nmynt
    return nmynt, nkrone


funksojner = [ett_og_ett_kast, vektoriserte_kast]
for funksjon in funksojner:
    # Pakker returverdiene ut av tuple til to eller flere variabler
    number = 1000
    nmynt, nkrone = funksjon(nkast=number)
    print()
    print("Mynt: ", nmynt, "\nKrone: ", nkrone)
    tid = timeit(partial(funksjon, nkast=number), number=1000)
    print("Tidsbruk: ", tid)


# 20 sidet terning
def best_av_to_d20(nkast: int) -> np.ndarray:
    kast = npr.randint(1, 21, size=(nkast, 2))
    # axis = 0: best av nkast (ikke relevant), axis=1: best av 2
    beste_kast = np.amax(kast, axis=1)
    return beste_kast  # Array med alle de beste kastene: size(nkast, 1) (nkast*1)


terningkast = best_av_to_d20(10000)
for resultat in range(1, 21):
    print(resultat, np.sum(terningkast == resultat))
print()
print("Gjennomsnitt: ", np.sum(terningkast) / len(terningkast))

plt.hist(terningkast, bins=20, rwidth=0.7)
plt.show()
