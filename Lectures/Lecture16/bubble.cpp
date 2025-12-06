#include <iostream>
#include <vector>

// NOTE: Bruker referanser slik at argumentene til funksjonen faktisk byttes om
// og ikke bare parametrene internt i funksjonen. Vil vil bytte om originalene
// ikke bare kopiene av dem.
void swap(int &a, int &b)
{
    int temp = b;
    b = a;
    a = temp;
}

void bubble_sort(std::vector<int> &input)
{
    // SKriver ut de 3 første elementene bare for å se sorteringen i aksjon
    std::cout << input[0] << ", " << input[1] << ", " << input[2] << std::endl;
    bool swapped;
    for (int stop_i = input.size() - 1; stop_i > 0; stop_i--)
    {
        swapped = false;
        for (int i = 0; i < stop_i; i++)
        {
            // Hvis de er i feil rekkefølge
            if (input[i] > input[i + 1])
            {
                swap(input[i], input[i + 1]);
                swapped = true;
                std::cout << input[0] << ", " << input[1] << ", " << input[2] << std::endl;
            }
        }
        if (!swapped)
            return;
    }
}

int main()
{
    std::vector<int> v = {2, 3, 1};
    bubble_sort(v);

    std::vector<int> u = {1, 3, 2};
    bubble_sort(u);

    std::vector<int> k = {1, 2, 3};
    bubble_sort(k);
}
