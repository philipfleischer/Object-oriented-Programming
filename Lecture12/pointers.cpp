#include <iostream>

int main() {
    int primes[] = {2,3,5,7,11, 0}; //0 er 0-pointer - quick patch fix

    std::cout << primes << std::endl;
    //Peker til minneadressen til første element i array
    int *ptr = primes;

    //Kan bruke pekeren til å navigere gjennom array:
    while (*ptr != 0) {
        std::cout << *ptr << std::endl;

        //Øker minneadressen med 1 int-lengde
        ptr += 1;
    }
    return 0;
}