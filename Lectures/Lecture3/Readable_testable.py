# God stil: Import øverst og på separate linjer
import math as m
import numpy as np
import scipy as sp

# Dårlig stil: Import midt i koden og på samme linje
import math, numpy, scipy

#God stil: Navn på klasser med stor forbokstav uten underscore
class EnKlasse:
    """Klasse som ike gjør noe som helst"""
    pass

# Unntak: Noen innebygde klasser i Python har ikke stor forbokstav
noen_innebygde_typer = [int, list, dict, str, bool]

# God stil: Konstanter med kun store bokstaver
EN_KONSTANT = 42

# NOTE: Ellers bør variabelnavn på ett tegn begrenses til matematikk
x = 3
g = 9.81 # Unntak fra sto bokstav på konstant (følger konvensjonen)

# Kan skrive ut docstring
print()
print(en_funksjon.__doc__ + "\n")
print(EnKlasse.__doc__ + "\n")

#OGså for innebygde og importerte typer (og biblioteker)
print()
print(list.__doc__)
print()
print(math.sin.__doc__)
print()
print(math.__doc__)


