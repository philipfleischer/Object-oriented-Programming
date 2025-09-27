#include <fstream>
#include <iostream>
#include <stdexcept>

int main() {
    //Array med 10 elementer av type Double (64-bit flyttall)
    //Typen SER UT TIL å være double, men [n] gjør det likevel til et array
    int n = 10;
    double en_array[n];

    //Å skrive ut en array skriver bare ut minneadressen
    std::cout << en_array << std::endl;

    //I C++ vil * foran noe som er en minneadresse gi oss det
    // som ligger på den adressen i minnet
    //MEN i en array blir det bare det første elementet som printes
    std::cout << *en_array << std::endl;

    //Må printe ved hjelp av en løkke for å få alle elementene
    for (int i = 0; i < n; i++) {
        //Skriver ut elementene i arrayet og plassen deres i minnet
        std::cout << "[" << i << "] før: " << en_array[i] << std::endl;

        en_array[i] = 0; //Implisitt konvertering fra int til double
        std::cout << "[" << i << "] etter: " << en_array[i] << std::endl;
    }

    //Vi kan også gi en array verdier direkte (får da automatisk rett lengde)
    int primes[] = {2, 3, 5, 7, 11};

    //hvordan kan vi finne lengden av en array generlt?
    //sizeof() gir oss hvor mye minne en variabel bruker
    std::cout << "Minne brukt av primes: " << sizeof(primes) << " bytes" << std::endl;
    std::cout << "Minne brukt av ett element i primes: " << sizeof(primes[0]) << " bytes" << std::endl;

    /*'Selvfølgelig' kan vi ved å sammenligne disse finne antall elementer
    Vi antar alle elementene i arrayet tar like mye plass, dermed kan vi finne
    antall elementer ved å dele størrelsen av alle elementene i arrayet
    med ett element i arrayet for å finne hvor mange ganger man får plass
    til det elementet, som vil si antall elementer i arrayet
    */
    int len_primes = sizeof(primes) / sizeof(primes[0]);
    std::cout << "Antall elementer i primes: " << len_primes << std::endl;

    //Skriver array til fil
    std::ofstream ofs("array.txt");
    if (!ofs) { throw std::runtime_error("Unable to open array.txt"); }

    for (int i = 0; i < len_primes; i++) { ofs << primes[i] << std::endl; }

    return 0;
}