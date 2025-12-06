Forelesning 22 - Profilering og Optimalisering - fredag 7/11

Læremål: Algoritmeanalyse og optimalisering
profilering: finne galskehalser (10% av koden bruker vanligvis 90% av tiden).

Monte Carlo-integrasjon eksempel modell, se på dette til eksamen?

Når skal vi optimalisere kode?

1. Få de til å virke. Ikke tenk på kjøretid here, test grundig og nøye at det virker
2. Få det til å virke bra. Gjør koden leselig og enkel å vedlikeholde. Del opp i klasser/funksjoner, lag bedre variablenavn, osv.
3. Få det til å virke bra og raskt. Finn flaskehalsene og se om de....

Ulemper med optimalisering:

- Tar tid fra andre ting (ny funksjonalitet, bedre testing, osv.)
  Kan gå ut over leseligheten ( i noen tilfeller) - hva er viktigst?
  Kan resultere i bugs.
  ...

Hvis vi skal optimalisere, hvordan gjør vi det?
Analysere algorithmer for å finne den teoretiske foskjellen mellom ulike fremgangsmåter.
Ta tiden på koden (benchmarking) for å finne ut hvor rask den er i praksis.
Profilering for å forstå hvilke deler av koden vi trenger å optimalisere.

Benchmarking:
Noe som ble brukt for å sammenligne våpen.
Det variert med hvor god skytteren (marksman) var med akkurat det våpenet, så for å eliminere den variablen festet man våpenet til en benk ...
I kodesammenheng er det vitkgi at man da tester ulike versjoner av koden mot samme benchmark ( og ikke endere test-caset over tid).
Kan da teste uliek tilnærminger med samme input og ...
