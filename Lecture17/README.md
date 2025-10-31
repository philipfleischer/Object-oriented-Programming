Forelesning 17 - Tilfeldighet. 20.10.25

Tilfeldige tall og simulereinger:
Tilfeldighet brukes i mange vitenskapelige sammenhenger
Sannsynlighet / statistikk
...

Hvor tilfeldige er tilfeldige tall?
Egentlig ikke tilfeldige i det hele tall - datamaskiner er deterministiske.
Hvis man gir RNG (random num gen) samme start-tilstand (seed) vil den alltid gjenskape de samme tallene
Derfor viktig å ikke starte med et fast seed, da vil programmet bare få de samme tallene hver gang det kjøres.
En mulighet er å bruke antall sekunder siden midnatt 1.jan 1970 (time.time() i Python) som seed, siden dette vil være forskjellig hver gang.

Pseudorandom numbers:
Selv om tallene eikke er rilfelsige, men er fast bestemt av seed, så ønsker vi at de skal komme ut i en rekekfølge som er statistisk fordelt slik ekte tilfeldige tall ville vært.
Dette er faktisk nok for våre formål.
pRNG =pseudoRandomNumberGenerator

Hva med repetisjoner?
Hvis hvert nye tall som generes kun er avhengig av forrige tall i rekken, vil enhver repetisjon av ett tall repetere alle tallene som kom etter det tallet.
Men i en tilfeldig tallrekke kan repetisjoner forekomme.
Enkel løsning: hvvis hvert nye tall i stedet avhenger a de siste 2 ellr 3 tallene, kan vi repetere ett enkelt tall uten at det blir problemer.
Men repeter vi lenge nok kommer vi til utgangspunktet.

Perioden til en pRNG
Viktig at algoritmen kan gå veldig lenge før den kommer tilbake til start-tilstanden hvor den vil begynne på nytt.
Mersenne Twister-algoritmen (som brukers av Random-biblioteket i Python) kan produsere 2^19937 - 1 unike tall før den kommer tilbake til start.
Disse tallene danner da basisen for tallrekker som er (statistisk sett) tilfeldig fordelt.

Sannsynlighet:
En lang pseudorandom tallrekke kan brukes til å produsere unirmt fordelte desimaltall mellom 0 og 1.
Hvis vi f.eks vil ha tall mellom 5 og 10 kan vi ta y = 5x + 5 der x e [0,1)
Kan også konvertere til andre sannsynlighetsfordelinger.

OBS: rand() i C++ lager problemer:
Lager samme tallrekke hver gang vi bruker rand()
Må gi den et seed - med f.eks srand(time(nullptr)) - for å få en ny tallrekke hver gang.
Bare garantert på en periode op minst 32000 tall - alt for lite for vitenskapelig anvendelse.

Velg riktig bibliotek!
Skal du lage noe som har med kryptering og sikkerhet å gjøre? import secrets
Trenger du mange tilfeldige tall på en gang? import numpy
