from typing import Iterator
import sys


def get_list(n: int) -> list[int]:
    """Lager en liste med tall i minnet på maskinen."""
    lst = []
    for i in range(n):
        lst.append(2 * i + 1)
    return lst


def get_iter(n: int) -> Iterator[int]:
    """Produserer de samem elementene når de trengs, i stedet for å lagre alle på forhånd i minnet."""
    for i in range(n):
        # Returnerer denne verdien, neste gang iteratoren trenger denne verdien så returneres den neste?
        # Den fortsetter å gi verdien til løkken er ferdig.
        # i motsetnign til vanlige funksjoner som får input og gir output, så går denne rekursivt?
        yield 2 * i + 1


tall_list = get_list(100000)
for i in tall_list:
    print(i)
print()
print(tall_list)
print()
print()

# Denne lager ikke en liste og lagrer det i minne som er veldig, smart siden vi slipper å lage og lagre
# datastrukturer, men kan heller bare lage midlertidige og bruke dem eller noe?
tall_iter = get_iter(100000)
for i in tall_iter:
    print(i)
print()

print(tall_iter)
print()

print("tall_list bruker", sys.getsizeof(tall_list), "bytes av minnet.")
print("tall_iter bruker", sys.getsizeof(tall_iter), "bytes av minnet.")
print()
# tall_list bruker 800984 bytes av minnet. dette er hvis vi skriver  get_list(100 000) og get_iter(100 000)
# tall_iter bruker 200 bytes av minnet.
