#include <iostream>

//returnerer true hvis n er primtall, false ellers.
bool is_prime(int n) {
    if (n == 1) {
        return false; //Liten f i false i c++
    }

    //While løkke
    int i = 2;
    while (i < n) {
        if (n % i == 0) { return false; }
        i = i+1;
    }
    return true;
}

int main() {
    //denne tilsvarer for i in range(1, 12, 1)
    for (int i = 2; i < 12; i++) {
        if (is_prime(i)) { std::cout << i << " is prime" << std::endl; }
        else { std::cout << i << " is NOT a prime" << std::endl; }
    }

    return 0;
}