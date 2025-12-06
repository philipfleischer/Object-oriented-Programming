import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

np.random.seed(12345)  # Ikke gjør dette i prosjekt 3

N = 10000  # Antall steg
X = np.zeros(N + 1)  # Posisjoner fra N=0 til og med N=10

# treigt
"""
X[0] = 0
for i in range(N):
    K_i = 2 * npr.randint(2) - 1
    X[i + 1] = X[i] + K_i

"""

# Raskere
K = (
    2 * npr.randint(2, size=N) - 1
)  # En-dimensjonal array, hvor elementene skal ha +1 eller -1
X[1:] = X[0] + np.cumsum(K)

print()
print(K[:10])
print(X[:10])
print()

# plt.plot(range(N + 1), X)
plt.step(range(N + 1), X, where="mid")
plt.xlabel("Antall steg")
plt.ylabel(r"$X_N$")
plt.show()
