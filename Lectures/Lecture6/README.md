Forelesning 6 - OOP -> Objekt Orientert Programmering

Læremål - Avanasert bruk av Python

Hvorfor OOP?
En måte å tenke på som organiserer og gjør ting mer oversiktlig (i mange tilfeller)
I stedet for passive samliner med data (list, dict ++) som må sendes inn til funksjoner for å bli gjort noe med ...
... kan man lage litt mer selvstendige objekter som i tilleg til å inneholde data selv vet hva de skal gjøre med disse dataene
Passiv: resultat = gjør_noe_med(en_samling)
selvstendig: resultat = et_objekt.gjor(på_en_samling)


Fire fordeler med OOP (de fire pillarene):
1. Abstraksjon
2. Innkapsling
3. Arv
4. Polymorfisme

Abstraksjon:
I stedet for å ha 20 ulike funksjoner som gjør ting med kortstokker å holde styr på...
... samle alle funksjoenne som representerer en Kortstokk i en klasse som tar seg av alt dette.
(Et enkelt Kort kan være en klasse).
Da er ting som naturlig hører sammen på samme sted.
Importerer da 2 klasser i stedet for 20 funksjoner.

Innkapsling:
Med en ordbok vil alle data være synlig for programmet som bruker den.
I en klasse kan vi gjenmme bort interne data og funksjoner som "omverdenene " ikke trenger å vite.
Reduserer kompleksitet: fokus på hva og ikke hvordan.
Grensesnittet til klassen er navnet på de offentlige metodene (funksjoenne) og variablene som annen kode skal bruke.
Resten er internt (bare interessant for klassen selv).

Arv:
Vi kan lage generelle klasser som fungerer i mange tilfeller (Kort).
Og mer spesialiserte klasser some r tilpasset en bestemt bruk (KlassiskKort, PokemonKort).
Alt som er felles for disse klassene er samlet i "moderklassen" Kort, og arves av de spesialiserte klassene (mer oversiktlig).
De spesialiserte klassene inneholder da kun ekstra funksjoner og data som bare er relevant til deres spesielle bruk.

Polymorfisme:
De spesielle klassene teller også som eksemplarer av "moderklassen" sin (men ikke omvendt).
    Et KlassiskKort telels som Kort
    Et PomemonKort teller som Kort
    Men et Kort teller ikke som et PoekemonKort
"Søskenklasser" teller ikke som hverandres type
    Et KlassiskKort teller ikke som et PokemonKort

Exceptions fungerer ved at de arver av hverandre. Går fra Exception og så StandardError som arver fra exception osv.
Teller en ArithmetricError som en ZeroDivisionError? -> Nei, siden ZeroDivisionError arver fra moderklassen ArithmeticError.
Teller en ZeroDivisionError som en Exception? --> Ja, siden zero arver fra exception
Teller en OverFlowError som en ZeroDivisionError? --> Nei, disse er søsken
Hvordan fange opp både OverFlowError og ZeroDivsionError, men ikke TabError (i en og samme except-blokk)? --> Må finne noe som overFlowerror og zero arver fra -> arithmetic error, som ikke taberror arver fra.
Dette er det OOP gir oss, altså fange opp ting vi vil ha på en enkel og effektiv måte.


Metoder:
En vanlig funksjon kalles slik:
    en_returverdi = en_funksjon(et_argument)
Men vi kan også la et objekt kalle ena v sine funksjoner for oss
    dette kalles en metode

self:
klassen er felles oppskrift for alle objekter av en type
Men når vi kaller en metode så trenger vi ogte å vite akkurat hvilket objekt som kalte metoden.
Ulike objetker av samme type kan ha helt ulike data (for eksempel tallverdi og farge på et spillkort)
Derfor inneholder alle metoder en ekstra paramater som ikke puttes i paranetereser i metoden self

Når en metode kalles:
- et_objekt.gjør_noe()
- et_objekt.gjør_noe_med(et_argument)
gjør pythonegentlig dette:
- Klassen til Objektet-.gkør noe (et objekt)
osv...

























