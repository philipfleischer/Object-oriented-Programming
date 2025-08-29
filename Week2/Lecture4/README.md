Notes from Lecture 4 IN1910 fredag 29/8

Testing

nyttige verktøy: assert, exceptions, pytest, TDD, exit-koder, 

Finnes mange typer exceptions. 

Fordeler med assert:
    - assert går fort å legge inn i koden
    - assert kan skrus av i "optimized mode"
        - Når vi har assert direkte i programmer og ikke kjører det med pytest
        - python -O program.py vil ignorere alle asserts og ikke gi AssertionError noe sted
        - Kan bruke logger i stedet for at programmet stopper opp ved en assertionerror

Fordeler med exceptions:
    - exceptions gir mer detaljert infor om hva som gikk galt

så hva bør jeg bruke når?
    - Bruk assert for å teste for feil som normalt aldri bør skje
    - Bruk exceptions for å teste for feil som kan forventes å skje når brukere kjører programmet
    Du kan tenke på assert som et utviklingsverktøy og exceptions som en naturlig del av brukeropplevelsen.

Enhetstesting (unit tests):
    - En "unit" er en liten del av et større program
    - Tester om delen fungerer
    - Lag tester samtidig som funksjonaliteten i programmet
    - kjøres automatisk.

GitHub Actions?
    - Kommer kanskje senere
    - Lar deg kjøre alle testene hver gang du gjør en commit, så du vet om koden i en branch begynner å se klar ut for merging
    - sjekke om det er god Kodestil


Feil med avrunding: Handler om å bruke pytest sin funksjon approx() for float numbers, siden de ikke blir riktig konvertert etter det vi ønsker akkurat nå
