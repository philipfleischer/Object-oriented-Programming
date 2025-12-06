from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as npr

npr.seed(12345678)

# possible_steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
possible_steps = [(1, 1), (-1, -1), (-1, 1), (1, -1)]  # Roterer 45 grader

# Uten vektorisering

N = 100  # Antall steg
Rs = np.zeros((N + 1, 2))  # Posisjon (steg, dimensjon: x & y)

for i in range(N):
    step = possible_steps[npr.randint(4)]  # Random trekk fra 0-3
    Rs[i + 1] = Rs[i] + step

# Dekomponerer vi X og Y fra R
Xs = Rs[:, 0]
Ys = Rs[:, 1]

plt.plot(Xs, Ys)
plt.axis("equal")
# markerer utgangspunktet (origo) med en sirkel
plt.scatter(0, 0, marker="o", color="black", s=100)
plt.show()

# med vektorisering
N = 100  # Antall steg
Rs = np.zeros((N + 1, 2))
steps = 2 * npr.randint(2, size=(N, 2)) - 1  # Steg
Rs[1:, :] = np.cumsum(steps, axis=0)

# Dekomponerer vi X og Y fra R
Xs = Rs[:, 0]
Ys = Rs[:, 1]

plt.plot(Xs, Ys)
plt.axis("equal")

plt.scatter(0, 0, marker="o", color="black", s=100)
plt.show()

# MAnge walkers

N = 500
nwalkers = 5

for walker in range(nwalkers):
    Rs = np.zeros((N + 1, 2))
    steps = 2 * npr.randint(2, size=(N, 2)) - 1  # Steg
    Rs[1:, :] = np.cumsum(steps, axis=0)

    # Dekomponerer vi X og Y fra R
    Xs = Rs[:, 0]
    Ys = Rs[:, 1]

    plt.plot(Xs, Ys, alpha=0.4)
    plt.scatter(Xs[N], Ys[N], marker="o", s=100)

plt.axis("equal")
plt.scatter(0, 0, marker="o", color="black", s=100)


# Plotte analytisk RMS
# rms = np.sqrt(
#    2 * N * np.sqrt(2)
# )  # Ekstra faktor sqrt(2) fordi ett steg ikke her lengde 1 når vi går på skrå
rms = np.sqrt(2 * N)
theta = np.linspace(0, 2 * np.pi, 1001)
plt.plot(rms * np.cos(theta), rms * np.sin(theta), "k--")
plt.show()
