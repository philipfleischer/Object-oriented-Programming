import matplotlib.pyplot as plt
import numpy as np

seed = 1916

# pRNG - pseudo random number generator
rng = np.random.default_rng(seed)

# --- Oppgave 1a ---

N = 50  # Antall steg
Xs = np.zeros(N + 1)  # posisjoner (1D-array). Fyll X med nuller -> zeros()

# Egen array med n-verdier (tid)
ns = np.arange(N + 1)

# Tilfeldige steg (med rng-objeckter): -1, 0 eller 1
dxs = rng.integers(low=-1, high=2, size=N)

# X[0] allerede lik 0
Xs[1:] = np.cumsum(dxs)

plt.step(ns, Xs, color="blue")
plt.xlabel(r"Step nr. $n$")
plt.ylabel(r"Position $X_N$")
plt.title("Plot of single walker in 1D")
plt.show()

# --- Oppgave 1b ---

N = 500  # Antall steg
W = 1000  # Antall walkers
Xs = np.zeros((N + 1, W))  # posisjoner (2D-array)

# Egen array med n-verdier (tid)
ns = np.arange(N + 1)

# Tilfeldige steg (med rng-objeckter): -1, 0 eller 1
dxs = rng.integers(low=-1, high=2, size=(N, W))

# X[0, :] allerede lik 0
Xs[1:, :] = np.cumsum(dxs, axis=0)  # Hvorfor axis=0, eksamen?

# Bruker alpha for å gjøre gjennomsiktighet (98% gjennomsikthighet)
plt.step(ns, Xs, color="blue", alpha=0.02)
plt.xlabel(r"Step nr. $n$")
plt.ylabel(r"Position $X_N$")
plt.title("Plot of {W} walker in 1D")
plt.show()
