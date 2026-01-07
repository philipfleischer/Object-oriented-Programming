#include <iostream>
int main(){
    //Som i python: Ikke-muterbar type gjør at vi ikke kan endre en verdi,
    // men lager en ny, dvs. a blir et nytt objekt, mens b er uendret
    // (gjelder ikke for muterbare typer som kan endre seg)
    int a = 1337;
    int b = a;
    a += 6440;

    std::cout << " a: " << a << "(" << &a << ")" << std::endl;
    std::cout << " b: " << b << "(" << &b << ")" << std::endl;

    //Med pekere kan vi endre både a og b selv om int er en ikke-
    // muterbare type (dette går ikke i Python)
    int e = 1337;
    int *f = &e;
    e += 6440;

    std::cout << " e: " << e << "(" << &e << ")" << std::endl;
    std::cout << " f: " << *f << "(" << f << ")" << std::endl;

}