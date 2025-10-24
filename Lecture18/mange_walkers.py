import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

npr.seed(12345)

n = 10000  # Steg per walker
nwalkers = 100  # Antall walkers

# Matrise: rad = steg, kolonne = walkers
X = np.zeros((n + 1, nwalkers))
X[0, :] = 0  # Startposisjon (unødvendig her, men for eksempelets skyld)

K = 2 * npr.randint(2, size=(n, nwalkers)) - 1
X[1:, :] = np.cumsum(K, axis=0)  # Summer over steg

N = np.arange(n + 1)

plt.plot(X)
plt.xlabel("Antall steg")
plt.ylabel("Posisjon")
plt.show()

# alpha = gjennomsiktighet i % for overlapp
plt.plot(X, alpha=0.01, color="k")
# Plotter teoretisk RMS (ROUTE MIN SQUARE)
plt.plot(N, np.sqrt(N), color="C1")
# Negativ:
plt.plot(N, -np.sqrt(N), color="C1")
plt.xlabel("Antall steg")
plt.ylabel("Posisjon")
plt.axis((0, 1000, -100, 100))
plt.show()

# Regner ut observert RMS (kan være forskjellig fra analytisk)
RMS = np.sqrt(np.mean(X**2, axis=1))  # axis=1 vil si snitt av walkers
plt.plot(N, RMS, label="Observed RMS")
plt.plot(N, np.sqrt(N), "--", label="Analytisk RMS")
plt.legend()
plt.xlabel("Antall steg")
plt.ylabel("RMS av avstand til utgangspunktet")
plt.show()
