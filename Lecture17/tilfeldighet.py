from random import seed, random
from matplotlib import pyplot as plt
import numpy.random as npr
from numpy import linspace
from scipy.stats import norm

from matplotlib.pylab import rand

# Fast seed - nyttig for testing
seed(1234)

print()
print("Samme hver gang: ", random(), random(), random())

# Tilfeldig seed - standard
seed()

print()
print("Ulikt hver gang: ", random(), random(), random())

# Mange tilfeldige tall? Bruk numpy isteden
print()
print(npr.random(size=30))

# Flerdimensjonal array (matrise)
print()
print(npr.random(size=(3, 3)))

# Hvilken sannsynelighetsfordeling får vi?
samples = npr.random(
    size=500
)  # Hvis vi øker til 50 000, så vil fordelingen bli jevnere
plt.hist(samples, bins=10, rwidth=0.7)
plt.show()
print()
print(npr.random(size=30))

# Uniform fordeling mellom andre tall enn 0 og 1
xmin = 10
xmax = 20
samples = npr.uniform(xmin, xmax, size=500000)
plt.hist(samples, bins=10, rwidth=0.7)
plt.show()

# Normalfordeling
gjennomsnitt = 16
standardavvik = 1
samples = npr.normal(gjennomsnitt, standardavvik, size=1000000)
plt.hist(samples, bins=10, density=True, rwidth=0.7)

xmin = 10
xmax = 20
xs = linspace(xmin, xmax, 1001)
print(xs)
ys = norm.pdf(xs, gjennomsnitt, standardavvik)
plt.plot(xs, ys, "--")
plt.show()
