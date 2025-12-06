Forelesning 18 Virrevandring (Random Walks) 23.10.2025

Endimensjonal Random Walker
Den vil øke med 1 eller -1, det er 50% sjanse uansett vei (mynt og kron).
x_N+1 = x_N + k_N

Ting vi kan modellere med virrevandring:

- Priser på aksjer,
- Populasjoner i biologi
- Genetiske endringer
- Polymerer
- Bildeprosessering
- Sammenligne søkemoterer på nett

2D-array: Første indeks rad, andre indeks kolonne (her s for steg og w for walker)
X = |S0W0 SoW1|
|S1W0 S1W1|

En liten analyse: <X_N+1> = <X_N + K_N>.
<X_N+1> = <X_N> + <K_N>.
<K_N> = 1/2*1 + 1/2*(-1) = 1/2-1/2 = 0
<X_N+1> = <X_N>
<X_N> = 0

Dette er gjennomsnittet. Tendens til at walkers begynner på samem punkt, men sprer seg og avviker fra gjennomsnittet. Dermed kan man måle gjennomsnittlig avvik fra gjennomsnittet.

Gjennomsnittlig avvik er generelt ikke et nyttig spredningsmål.
Positive og negative avvik fra snittet nuller hevrandre ut.
Ingen forskjell på ingen spredning og symmetrisk spredning!
I stastistikk regner vi isteden ut det gjennomsnittlige kvadratsavviket slik at både negative og positive avvik bidrar til spredningsmålet.
Dette brukes så ofte at det har fått navnet varians.
For å få samme enhet som et datapunkt og snittet tar vi ofte kvadratroten etterpå.

En litt mer meningsfull analyse:
Se forelesnings slide!
...

Dermed kan vi finne variansen fra <X^2_N> = N.
Varians er gjennomsnittlig kvadrat-avvik: <(X_N - <X_N>)^2>
= <X^2_N -2X_N<X_N> + <X_N>^2>
= <X^2_N> fordi <X_N> = 0.
Var(X_N) = N.
...

Vi kan også finne RMS (Route Mean Square):
<X^2_N> = N,
RMS = sqrt(<X^2_N>) = sqrt(N).

OBS: RMS er bare likt standardavviket når gjennomsnittet er 0.

OBS: Store avvik teller mer enn små:
Gjelder både variant/standardsavvik og RMS
-1 -1 1 1 -> variant og RMS 1, standardavvik 1
-8 -8 8 8 -> variant og RMS 64, standardavvik 8
-8 -1 1 8 -> variant og RMS 32.5, standardavvik 5.7

    - Altså ikke 4.5 som er det gjennomsnittlige avviket!
    - De store avvikene vektes mer enn de små selv i stnadardavviket.

Hva blir standardavviket av de syv tallene -4 -2 1 1 1 1 2?

    - (det gjennomsnittlige avviket blir 12/7 = 1.71)
    - Svaret: 4^2 + 2^2 + 1^2 + 1^2 + 1^2 + 1^2 + 2^2 = 28
    28/7 = Noe som er større en standardavviket over.
