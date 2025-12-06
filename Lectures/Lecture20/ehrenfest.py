import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

# Oppsett av plot
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["xtick.labelsize"] = 14
plt.rcParams["ytick.labelsize"] = 14
plt.rcParams["axes.titlesize"] = 16
plt.rcParams["axes.labelsize"] = 16
plt.rcParams["lines.linewidth"] = 2

# Slik at vi alle får samme "tilfeldige" figur
npr.seed(123456789)

N = 100  # antall steg
B = 20  # antall baller

# Systemets tilstand i hvert steg = antall baller i venstre krukke
Xs = np.zeros(N + 1)
# Start-tilstand: alle 20 ballene i høyre krukke: Xs[0] = 0

ks = np.arange(N + 1)

for k in range(N):
    ball = npr.randint(20)  # indeks 0..(N-1) for en tilfeldig ball
    if ball < Xs[k]:
        Xs[k + 1] = Xs[k] - 1  # vestre --> høyre

    else:
        Xs[k + 1] = Xs[k] + 1  # vestre <-- høyre

plt.step(ks, Xs, where="mid")
plt.axhline(B / 2, linestyle="--", color="black")  # Midtlinje: 10 i hver
plt.axis((0, N + 1, 0, 20))
plt.xlabel(r"Steg $k$")
plt.ylabel(r"Tilstand $x$")
plt.show()
