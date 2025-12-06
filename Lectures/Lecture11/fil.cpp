#include <iostream>
#include <fstream>
#include <string> 

int main() {
    // Åpne fil for skriving (ofstream = out-file srteam)
    // får feil hvis mappen ikke finnes slik: tmp/output.txt
    std::ofstream ofs("output.txt");

    //Vi sjekker om vi klarte å åpne filen for skriving
    if (! ofs) {
        //raise exception (når filen KJØRES, ikke kompileres)
        throw std::runtime_error("Unable to open file");
    }

    //Skriver 0-9 i ouput.txt filen (samme som file.write())
    for (int i = 0; i < 10; i++){
        ofs << i << std::endl;
    }

    //variabel uten verdi: Tar det som er i minnet fra før
    // og tolker som en int (vet at en int er 32 bytes?)
    int x;
    ofs << "x før den får verdi: " << x << std::endl;

    // in-file stream for lesing av fil
    std::ifstream ifs("output.txt");

    //eof = end of file
    //ifs.eof() returnerer true så lenge vi ikke er komem til slutten
    std::string lest_linje;
    while (! ifs.eof()) {
        // gå til neste linje
        std::getline(ifs, lest_linje);

        //skriv ut til terminal:
        std::cout << lest_linje << std::endl;
    }
     
    return 0;
}