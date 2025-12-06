Forelesning 20 - Markov-Kjeder - 31.10.2025

RMS for 2D-vandreren vår:

Sum over en akse:
Det høres lite intuitivt ut, men...
For å ta summen av hver rad
Må vi ta summen over alle kolonenne
Det er denne siste som bestemmer axis=1
Så selv om rad er den første indeksen (axis=0) er det altså ikke den vi bruker til å finne summen av en rad.
...

Markov-kjeder:

Ehrenfest-eksperimentet:
Tre baller i venstre krukke = tilstand D
7 baller i høyre krukke
sannsyneligheten for at vi flytter tre kuler fra venstre til høyre er p=3/10 og motsatt p=7/10

Hva kommer til å skje med sannsyneligheten over tid? Bli 0?

Analyse av ehrenfest-eksperimentet:
a given probability vector, (complement) p. This vector would be m + 1 elements long, and the element pi would express the probability that the systen is in state i. As this probability changes over time, we will denote the probability vector after N steps as (complement) pN.
As the system starts in x=0, we know that
(complement) p0 = (1,0,0,...,0)

For the first step of the iteration, we know we will have to move x=1 with 100% likelihood, so we get (complement) p0 = (1,0,0,...,0).

But what happens now? The prob of moving another ball from the right urn to the left is 19/20, ie.e, 95%. But there is a small chance of 1/20, or 5%, of moving the ball back. Thus the prob vector splits:
(complement)p2 = ((1/20), 0, ...)...
...

For å regne videre på dette setter vi oppe n forplantningsmatrise (propagator matrix) som lar oss regne ut sannsyneligheten i neste steg basert på hvordan sannsynligheten er fordelt i forrige steg.
...
...
...
