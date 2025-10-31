Forelesning 10 - Objektorientert Design og Funksjoenr som Objekter i Python.

Fortsetter på forelesning 11 også!!!


Noen begreper (prosjekt 1):
- Overload = flere metoder med samme navn og ulike parametere.
    - def spill_kamp(self, k: Kamp) -> None:
    - def spill_kamp(self, hjemmelag: Lag, bortelag: Lag) -> None:
    - Funker ikke direkte i Python - den siste overskriver den første!
- Override = overskrive metode fra foreldreklassen (ved arv)
    - KlassiskKortstokk.__init__ kan gjøre noe annet enn Kortstokk.__init__
    - Pendulum_create_result kan gjøre noe annet enn ODEModel._create_result

Læremål: Avansert bruk av Python:
- Objektorientert programmering er en måte å tenke på når vi skriver programmer som åpner nye muligheter


Hva er vitsen med docstrings?
Svar fra menti:
    - Hjelpe brukeren med å benytte seg av ett objekt på korrekt måte.
    - Forkare for brukere av funksjonen, hva den gjør. 
    - Dokumentere hvordan bruke en funksjon/klasse/fil etc.

Hva er et grensesnitt?
Svar fra menti:
    - Interface er kontaktflaten mellom to systemer.
    - De offentlige funksjonene som skal brukes utenifra og ikke privat inne i filen.
    - Grensesnittet sier hva vi kan gjøre, mens implementasjonen sier alt. Grensesnittet kan tenkes på som grensen av de som skal bruke systemet og de som skal lage og jobbe med systemet. En bilmekaniker trenger kunnskap om mye innvendig i bilen, men en lege trenger kun vite hvordan man kjører bilen og ikke hvordan den er bygget opp.
    - Reduserer kompleksiteten til systemet for brukerne enormt.
    - Dokumentasjon er en del av grensesnittet (som bil manual).

Hvor viktig er det å dokumentere følgende?
    1. Hva koden gjør:
        Dette er det viktigste, å dokumentere koden. 
    2. Grensesnittet til klasser og funksjoner
        Veldig god nummer to, sidene det er viktig å vite hvordan man bruker disse tingene.
    3. Avansert Python-syntaks (teknsike finurligheter)
        Dette er viktig å dokumentere, men her bruker man heller kommentarer i stedet for å bruke docstrings.
    4. Grunnleggende Python-syntaks
        Kun i undervisningssammenheng vil dette være nødvendig (det er som å markere at å løpe er et verb, for de som ikke visste dette).

Hva er poenget med å kjøre python-program med kommandoen "python -O filnavn.py"?
    - Setter variabelen __debug__ = False.
        Dete gjør at asserts blir oversett, slik at programmet kjører uten å få feilmaeldinger. (Vi har testfiler, så dette er ikke viktig, men mange har asserts i vanlig hovedfil).

Hvordan kan du se exit-koden til et Python-program i terminalen?
- Windows: "$LastExitCode" i Powershell
- Mac/Linux: "echo $?" i bash


Dataobjekter - én måte å jobbe på:
    - Prøv først med å arve fra NamedTuple
        - Hvis det ikek funker (f.eks, hvis noe må endres)...
    - Prøv en dataclass
        - Hvis det heller ikke funker
            (f.eks, hvis __init__ må gjøre mer enn å bare sette atributter)...
    - Bruk en vanlig klasse
        - (Fordel: Ingen import nødvendig)
    - Dette er ikke en regel: Bare et forslag til de tilfellene hvor man ikke vet helt hva man trenger!


Nesten alt i python er objekter!
    - Det tomme objektet None er et objekt (av klassen NoneType)
    - Funksjoner er objekter (av klassen function eller builtin_function_or_method)
    - Objekters metoder er objekter (av klassen method eller builtin_function_or_method)
    - Selv klasser er objekter (av klassen type).

    