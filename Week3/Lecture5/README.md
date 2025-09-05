Logging og Debugging Forelesning 5 mandag 01.09

Exit koder:
Noen ganger kjører et program et annet program, da er det ikke sikekrt vi vet hvilket av program som gir feil.
Dermed kan vi bruke: echo $? for å se forrige kjøring av program. 0 betyr suksess, 1 betyr noe gikk galt, 2+ er feilkoder man kan slå opp

Print statements for å finne feil:
Må fjernes etteropå, så brukere ikke ser det.
Bedre alt:
- Logging til fil eller terminal.
Det er flere nivåer av dette.

Python Tutor:
God visualisering av objekter, nyttig for å lage en emntal modell av hva som skjer i maskinen. Klarer ikek kjøre lange programmer. 2000 kodelinjer til sammen er maksimum.
All koden må være i samme fil, ikke bra. Det er reklame i den

Debuggeren i VS Code:
Kan pause programmet der vi vil og følge med på hva som skjer med objekter/ variabler
Eventuelt pause bare når en betingelse er oppfylt (for å slippe de 100 første stegene der feil ikke skjer).
Kan velge om vi vil jobbe på høyt nivå eller lavt nivå (om vi vil se inne i funksjoner eller bare overordnet over dem).
Kan endre verdier av variabler for å teste.
Kan printe til egen debug-terminal uten å printe til terminalen brukeren ser
