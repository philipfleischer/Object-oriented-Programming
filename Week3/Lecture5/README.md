Logging og Debugging Forelesning 5 mandag 01.09

Exit koder:
Noen ganger kjører et program et annet program, da er det ikke sikekrt vi vet hvilket av program som gir feil.
Dermed kan vi bruke: echo $? for å se forrige kjøring av program. 0 betyr suksess, 1 betyr noe gikk galt, 2+ er feilkoder man kan slå opp

Print statements for å finne feil:
Må fjernes etteropå, så brukere ikke ser det.
Bedre alt:
- Logging til fil eller terminal.
Det er flere nivåer av dette.