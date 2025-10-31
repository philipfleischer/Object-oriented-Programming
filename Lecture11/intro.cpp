// Kommentar i C++ / CPP

// import 
#include <iostream>
#include <string>

// returverdi først (i stedet for def)
// double er 64-bits flyttall (tilsvarer float i python)
double feet(double m) {
    return 3.28085 * m;
}

//Funksjon uten returverdi (tilsvarer None i python)
void greet(std::string name) {
    std::cout << "Hello there," << name << "!" << std::endl;
}

int main() {
    std::cout << "Hello World!" << std::endl;
    greet("gjeng");

    //variabler må ha typer i c++
    std::string name = "Bob";
    int birth_year = 1990;

    //Kalle funksjon med retuverdi
    std::cout << "2 m in feet = " << feet(2) << "m." << std::endl;

    double height_feet = feet(2.5);
    //Må ha parenetes rundt if-else
    if (height_feet < 7) {
        std::cout << "Height is less than 7 feet" << std::endl;
    }

    return 0;
}