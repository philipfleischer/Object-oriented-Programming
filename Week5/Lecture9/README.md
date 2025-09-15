Arv Lecture 9 Mandag 15/9

Læremål: Avansert bruk av Py

- OOP prog er en måte å tenke på når vi skriver programmer.
Ikke veldig sentralt med arv og OOP i den virkelige verden?

Bør vi alltid bruke arv?
Nei ikke alltid, arv kan være fornufting hvis vi skal lage en klasse som bruker det samem som en allerede eksisterende klasse den kan arve fra.
Dermed kan man oppdatere moderklassen uten å måtte oppdatere alle barne klassene hver for seg.
Type sjekking kan bli rotete, b: Bird er enklere enn b: Albatross, Dove, osv.


Hva er alternativet?
Duck typing (py):
- "if it.swim() like a Duck and .fly() like a Duck, it must be a Duck".


Fordeler med duck typing i py:
Koden blir enklere og fleksibel når du kan fokusere på hva objektene gjør og ikke hva de er
Du kan lage enkler prototyper av mer kompliserte klasser for å teste anenn kode i en tidlig fase
Du kan gjenbruke en klasse et annet sted uten å importere alle kalassene som arver fra hverandre.


Ulemper med duck typing:
Programmet kan kræsje elelr gi feilmelding nåpr det kjøres sinden det mangler en modetode eller atrbiutt som man antok var der.
...


Definere grensesnitt med abstract base class, (interface, ABCs):
En anen måte å bruke arv på
lager en abstrakt klasse = en du ikek kan lage objetker av (du kan ikke lage en swimming, men du kan lage en Duck).
En klasse som arver fra denne klasessen må implementere alle metodene i grensesnittet.
hvis du glemmer en får du NotImplementedError
Kan dermed tvinge et objekt til å ha bestemte moder fra et eller flere grensesnitt.


Kan arve fra flere klasser og ikke bare én.
Python støtter generelt arv fra flere kalasser samtidig. Det er viktig å eksplisitt si hvilke klasser vi arver fra når, istedet for å bare skrive super().__init__(), så må man skrive f.eks: Student.__init__(self) (ta med self også).




