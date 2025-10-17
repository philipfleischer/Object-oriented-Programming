#include <iostream>

using namespace std;

void call_by_value(int paramater)
{
    paramater = -1;
}

void call_by_reference(int &parameter)
{
    parameter = -1;
}

void call_by_pointer(int *parameter)
{
    *parameter = -1;
}

// Ikke erstattet arrayuen med en annen, dette er et muterbart objekt
//  kan endre tilstand over tid, vi endret det første elementet.
//  når vi holder på med muterbare objekter, så ...
void what_about_arrays(int parameter[])
{
    parameter[0] = -1;
}

int main()
{
    int original = 1;
    int kopi = original;
    int *peker = &original;
    int &referanse = original;

    cout << "Addresse til original: " << &original << endl;
    cout << "Addresse til kopi: " << &kopi << endl;
    cout << "Addresse til peker: " << &peker << endl;
    cout << "Addresse til referanse: " << &referanse << endl; // Samme minneaddresse som &original

    original = 2;

    cout << "original: " << original << endl;
    cout << "kopi: " << kopi << endl;
    cout << "peker: " << *peker << endl;
    cout << "referanse: " << referanse << endl;

    int argument = 42;
    call_by_value(argument);
    cout << "After call_by_value: " << argument << endl;
    call_by_reference(argument);
    cout << "After call_by_reference: " << argument << endl;

    argument = 42;
    call_by_pointer(&argument);
    cout << "After call_by_pointer: " << argument << endl;

    int argument2[] = {42};
    what_about_arrays(argument2);
    cout << "After what_about-arrays: " << argument2[0] << endl;
}
