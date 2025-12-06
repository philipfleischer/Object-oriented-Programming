Forelesning 12 - Arrays, Minne og pekere - C++

Arrays vs. Lister
- Array <---> Lenket liste
    Kun én datatype <---> Blande flere datatyper mulig
    Fast størrelse <---> Vokser og kryper etter behov
    Elementvise operasjoner <---> Må bruke løkke for å gjøre noe med alle elem
    Rask og spesialisert <---> Treig og generell
    Bruker indekser <---> Må alltid starte først/sist

Python-lister er strengt tatt en mellomting siden de har indeksering.

Litt om bits og bytes:
- En bit (binary digit) er et siffer i totallsystemet: 0 eller 1
- En byte er en etterlevning fra tiden da datamaskiner behandlet 8 bits av gangen (1 byte = 8 bit).
- 01001000 og 01101001 er eksempler på bytes i minnet.
    - Kan tolkes som bokstavene "H" og "i" (char)
    - Eller heltallene 72 og 105 (int)
- Nå behandler maskinene vanligvis 64 bits av gangen (8 bytes), men byte som enhet har overlevd av historiske årsaker.


Python har mer sikkerhetsnett enn C++ (C++ går ofte rett på minnet i maskinen).

Hva er en pointer (peker)?
- En variabel er et navn til en verdi som ligger i minne til maskinen.
- En peker er et navn vi gir til minneadressen til en slik verdi
- int e = 10 lagrer verdien 10 på minneadresse 0xA45C (tilfeldig adresse som varierer fra gang til gang).
- &e gir oss denne adressen (0xA45C) - tilsvarer id(e) i Python.
En peker int* e_sin_adresse = &e er en variabel hvor verdien er minneadressen til en annen variabel (målt i bytes).
- (og pekeren har også sin egen adresse, f.eks: 0xA3C2) 


Noen viktige spørsmål:
I know this is a really basic question, but i have just started with some basic C++ programming after coding a few projects with high-level languages (e.g. Python).
Basically I have three questions:
1. Why use pointers over normal variables?
Short answer is: Dont ;-) Pointers are to be used where you cant use anything else. It is either because the lack of appropriate functionalyity, missing data or for pure performance. More below...

2. When and where should i use pointers?
Pointers allow you to refer to the same space in memory from multiple locations. This means that you can update memory in one location and the change can be seen from another location in your program. 
You should use pointers any place where you need to obtain and pass around the address to a specific spot in memory. You can also use pointers to navigate arrays:

3. How do you use pointers with arrays?
