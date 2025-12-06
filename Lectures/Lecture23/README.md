Blandet programmering - Forelesning 23. Man 10.11.25

Kan blande flere språk for å gjøre det raskere. Blande C og python f.eks.

Profilering av minnebruk.

cProfile:
ncalls: The numer of times the function is called.
tottime: Time spent inside the funciton without sub-functions it calls.
cumtime: Time spent inside the function and inside functions it calls.
per call: cumtime fivided by the number of calls.

OBS: Kan variere med OS og maskin:
Python, Mypyc and PyPy har lang kjøretid.
NumPy, Numba, C++, C++ with Ctypes, Ctypes and ofast flag, Cppyy har kort kjøretid.
