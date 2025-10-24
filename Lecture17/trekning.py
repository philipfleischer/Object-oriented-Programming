from random import choice, choices
import numpy.random as npr

deltakere = [
    "Alfred",
    "Beatrice",
    "Charlie",
    "Danielle",
    "Ellinor",
    "Frederick",
    "Gabriel",
]

vinner = choice(deltakere)
print(f"En vinner: {vinner}")

vinnere = choices(deltakere, k=3)
print(f"Tre vinnere: {vinnere}")

unike_vinnere = npr.choice(deltakere, 3, replace=False)
print(f"Tre unike vinnere: {unike_vinnere}")
