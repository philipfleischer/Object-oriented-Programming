Referanser og sorteringsalgoritmer. 17.10.25

Læremål: Datastruktururer og algoritmer
Du har brukt arrays og lister i pyth
Her skal vi gå litt under panseret og se hvordan de fungerer, f.eks hvordan vi jobber med minnet på datamaskinen. Dette danner en bases for å kunne lage egne dataobjekter på en god måte detr det trengs.

L@remål: Algoritmeanalyse

Nytt begrep: Amortisert kjøretid
= avg runtime
Når både best case og worst case er sjeldne tilfelelr som ikke er represenattive, kan det være like nyttig å se på hvor lang tid en avg operasjon tar
Ser vii på summen av veldig mange operasjoner er det usannslyndlig at alle vil være worst case (ofte raskere i praksis.).

Amortisert kjørtid prosjekt 2
Instead og analyzing a single append, let us say we start with an empty dynamic array and append n element to it
ArrayList example;

for (int i = 0; i < n; i++) {
example.append(i);
}

What is the total cost of this operation, in Big O, as a function n? Each of the n appends cost O(1), so n operations of O(1) will cost a total of O(n).

Hva bør brukes i Prosjekt 3 oppgave 3?

- Worst case
- Amortisert
- Eventuelt begge
  Viktig for eksamen

I doxygen filen kan vi skrive USE_MD_FILE_AS_MAINPAGE = README.md

Hva betyr int& for noe?
Ikek noe symbol ->variabel int x = ... - verdi ..., = x;

- -> Peker (minneadresse) int *x = ... -> Verdi på minneaddresse ... = *x

& -> Referanse int&x = ... -> Minneadresse ... = &x

int y = x kopierer verdien til et annet sted i minnet (&y != &x)

int &y = x gjør at x og y peker på samme verdi (&y == &x)

C++ har to måter å overskrive (tilordne) flere variabler samtidig på ...

Men det gjelder overskriving av hele objektet, ikke endring av (muterbare) objekter.
