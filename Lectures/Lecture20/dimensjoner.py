import numpy as np
from sympy import rad

print("\nRadvektor:\n")
radvektor = np.zeros((1, 10))  # 1 rad, 10 kolonner
radvektor[0, :] = np.arange(0, 10)
print(radvektor)

print("\nKolonnevektor:\n")
kolonnevektor = np.zeros((10, 1))  # 10 rad, 1 kolonner
kolonnevektor[:, 0] = np.arange(1, 11)
print(kolonnevektor)

print("\nGangetabell:\n")
# Matrisemultiplikasjon: (10 x 1) * (1 x 10) = (10 x 10)
gangetabell = kolonnevektor @ radvektor
print(gangetabell)

print("\nradvektor @ kolonnevektor:\n")
# Matrisemultiplikasjon: (1 x 10) * (10 x 1) = (1 x 1) - Scalar product
print(radvektor @ kolonnevektor)  # NOTE: Fortsatt en 2D-array


print("\nradvektor * kolonnevektor:\n")
# Elementvis multiplikasjon (med samme dimensjoner)
print(radvektor * kolonnevektor)

print("\nradvektor * radvektor:\n")
# Elementvis multiplikasjon (med samme dimensjoner)
print(radvektor * radvektor)

print("\nkolonnevektor * kolonnevektor:\n")
# Elementvis multiplikasjon (med samme dimensjoner)
print(kolonnevektor * kolonnevektor)

print("\nradvektor @ radvektor error:\n")
# Ulovlig matrisemultiplikasjon: (1 x 10) * (1 x 10) =
try:
    print(radvektor @ radvektor)
except ValueError as e:
    print(e)

print("\nGangetabell sum (axis=0):\n")
# Summer over rader (axis=0) for å få summen av hver kolonne
print(np.sum(gangetabell, axis=0))

print("\nGangetabell sum (axis=1):\n")
# Summer over rader (axis=1) for å få summen av hver kolonne
print(np.sum(gangetabell, axis=1))

print("rader sum (axis=0):\n")
# NOTE: Begge sumene reduserer array fra 2D til 1D
# Kan gjøre om til hhv. rad- og kolonnevektorer i 2D etterpå
rad_2d = np.sum(gangetabell, axis=0)  # lir 1D-array
rad_2d.shape = (1, 10)
print(rad_2d)

print("\nkolonner sum (axis=1):\n")
kolonne_2d = np.sum(gangetabell, axis=1)  # lir 1D-array
kolonne_2d.shape = (10, 1)
print(kolonne_2d)
