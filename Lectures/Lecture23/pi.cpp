#include <chrono>
#include <cmath>
#include <iostream>
#include <numbers>

double estimate_pi(unsigned int N)
{
    double pi_divided_by_four = 0.0;
    for (unsigned int i = 0; i < N; i++)
    {
        // pow == ** == opphøyd
        pi_divided_by_four += std::pow(-1, i) * 1.0 / (2.0 * i + 1.0);
    }
    return 4.0 * pi_divided_by_four;
}

int main()
{
    int number = 1000;
    auto t_start = std::chrono::high_resolution_clock::now();
    double result;
    for (int i = 0; i < number; i++)
    {
        result = estimate_pi(100000); // Ikke rettferdig benchmark (ekstra tilordning)
        // Estimate_pi(1000); // Rettferdig benchmark
    }
    auto t_stop = std::chrono::high_resolution_clock::now();
    int ms = std::chrono::duration_cast<std::chrono::milliseconds>(t_stop - t_start).count();
    // Krever std=c++20 under kompilering for å få bort numbers squiggles:
    double relative_error = std::abs(std::numbers::pi - result) / std::numbers::pi;
    std::cout << "estimate_pi (C++)" << std::endl;
    std::cout << "Pi: " << result << std::endl;
    std::cout << "Rel. error: " << (100 * relative_error) << "%" << std::endl;
    std::cout << "Tidsbruk (1000x): " << (ms / 1000.0) << "s" << std::endl;
}
