# God stil: Import øverst og på separate linjer
import math as m
import numpy as np
import scipy as sp

# Prøver å lage TabError
if True:
    print("tab")
    print("spaces")

# Dårlig stil: Import midt i koden og på samme linje
import math, numpy, scipy

# Dårlig Stil: Dictionaries
forkortelser = {"B/G": "Bodø/Glimt", "BRA": "Brann", "TIL": "Tromsø", "LSK": "Lillestrøm"}

# God stil: 
forkortelser = {
    "B/G": "Bodø/Glimt", 
    "BRA": "Brann", 
    "TIL": "Tromsø", 
    "LSK": "Lillestrøm"
    }

# God stil: Små bokstaver og underscore på navn til variabler og funksjoenr
en_variabel = "En verdi"

def en_funksjon(en_parameter):
    """printer ut parameteres."""
    print(en_parameter)

#Dårlig stil: variabler og funksjoner ser ut som klasser
DårligVariabelNAVN = 2

def DårligFunksjonSNAVN():
    pass

#God stil: Navn på klasser med stor forbokstav uten underscore
class EnKlasse:
    """Klasse som ike gjør noe som helst"""
    pass

# Unntak: Noen innebygde klasser i Python har ikke stor forbokstav
noen_innebygde_typer = [int, list, dict, str, bool]

# God stil: Konstanter med kun store bokstaver
EN_KONSTANT = 42

# Dårlig stil: variabelnavn på ett tegn som kan forveksles.
1 = 1
0 = 0
I = 1

# NOTE: Ellers bør variabelnavn på ett tegn begrenses til matematikk
x = 3
g = 9.81 # Unntak fra sto bokstav på konstant (følger konvensjonen)


# God stil: bruk ellers mer beskrivende variabelnavn

#Python lar oss gjøre mye rart med whitespace
en_funksjon(21)     # :)
en_funksjon(21)     # :>

en_liste = [1,2,3,4,5]
en_liste = [1,2,3,4,5]
en_liste = [1,2,3,4,5]

en_element = en_liste