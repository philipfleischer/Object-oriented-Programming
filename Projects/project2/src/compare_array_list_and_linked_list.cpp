/**
 * @file compare_array_list_and_linked_list.cpp
 * @brief Comparing ArrayList and LinkedList performance for get and insert-front operations.
 *
 * This program compares the time complexity of get and insert funcitons for the two classes´s implementations. It is measuring the time taken for input size N, it computes average time per operation and writes results to .txt files.
 *
 * The results inside the .txt files are then used to plot the behaviour time for the different functions in 4 different graphs using plot_timings.py to visualize it.
 */

#include <chrono>    // for high_resolution_clock
#include <fstream>   // for ofstream
#include <iostream>  // for cout
#include <stdexcept> // for runtime_error

#include "array_list.h"
#include "linked_list.h"

using namespace std::chrono;

/**
 * @brief Measures the average time to acces the middle element in an ArrayList object.
 *
 * The list is filled with N elements, the program enters element at index N/2 1000 times and monitors the time for each one, then it calculates the average time per access in microseconds.
 *
 * Results are written to a file called "array_list_get.txt".
 */
void run_array_list_get()
{
    std::cout << "\nArray list - get" << std::endl;
    std::ofstream ofs{"gen/array_list_get.txt"};
    if (!ofs)
    {
        throw std::runtime_error("Unable to open file");
    }
    // Number of times we want to run the access
    int runs = 1000;
    // Growing N by a factor of 10
    for (int N = 100; N < 1E6; N *= 10)
    {

        ArrayList a = ArrayList();
        for (int i = 0; i < N; i++)
        {
            a.append(i);
        }
        auto start = high_resolution_clock::now(); // start timing
        // Get value in the middle
        for (int run = 0; run < runs; run++)
        {
            auto value = a[N / 2];
        }

        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<microseconds>(stop - start);
        std::cout << N << " " << duration.count() / (double)runs << "\n";
        ofs << N << " " << duration.count() / (double)runs << "\n";
    }
}

/**
 * @brief Measures the average time for front-insertions in a ArrayList object.
 *
 * This program inserts N elements into the front of the doubly linked list and computes the average insertion time.
 *
 * Results are written to a file called "array_list_insert.txt".
 */
void run_array_list_insert_front()
{
    std::cout << "Array list - insert front" << std::endl;
    std::ofstream ofs{"gen/array_list_insert.txt"};
    if (!ofs)
    {
        throw std::runtime_error("Unable to open file");
    }
    for (int N = 100; N < 1E6; N *= 10)
    {
        auto start = high_resolution_clock::now();
        ArrayList a = ArrayList();
        for (int i = 0; i < N; i++)
        {
            a.insert(i, 0); // Inserting at index 0 (front)
        }

        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<microseconds>(stop - start);
        std::cout << N << " " << duration.count() / (double)N << std::endl;
        ofs << N << " " << duration.count() / (double)N << std::endl;
    }
}

/**
 * @brief Measures the average time for accessing middle element in a LinkedList object.
 *
 * The list is filled with N elements, the program enters element at index N/2 1000 times. Accessing by index requires shifting of indexes in the list, therefore we expect linear time complexity.
 *
 * Results are written to a file called "linked_list_get.txt".
 */
void run_linked_list_get()
{
    std::cout << "Linked list - get\n";
    std::ofstream ofs{"gen/linked_list_get.txt"};
    if (!ofs)
        throw std::runtime_error("Unable to open linked_list_get.txt");

    const int runs = 1000;
    for (int N = 100; N < 1E6; N *= 10)
    {
        LinkedList dll;
        for (int i = 0; i < N; i++)
            dll.append(i);
        auto start = high_resolution_clock::now();

        for (int r = 0; r < runs; r++)
        {
            volatile int v = dll[N / 2]; // The linear time operation
            (void)v;
        }
        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<microseconds>(stop - start);

        double avg_us = duration.count() / static_cast<double>(runs);
        std::cout << N << " " << avg_us << "\n";
        ofs << N << " " << avg_us << "\n";
    }
}
/**
 * @brief Measures the average time for front-insertion in a LinkedList object.
 *
 * N elements inserted at head pointer in the list and that is in constant time complexity, therefore we expect constant time scaling for the function.
 *
 * Results are written to a file called "linked_list_insert.txt".
 */
void run_linked_list_insert_front()
{
    std::cout << "Linked list - insert front\n";
    std::ofstream ofs{"gen/linked_list_insert.txt"};
    if (!ofs)
        throw std::runtime_error("Unable to open linked_list_insert.txt");

    for (int N = 100; N < 1E6; N *= 10)
    {
        LinkedList dll;
        auto start = high_resolution_clock::now();

        for (int i = 0; i < N; i++)
            dll.insert(i, 0);

        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<microseconds>(stop - start);

        double avg_us_per_insert = duration.count() / static_cast<double>(N);
        std::cout << N << " " << avg_us_per_insert << "\n";
        ofs << N << " " << avg_us_per_insert << "\n";
    }
}

int main()
{
    run_array_list_get();
    run_array_list_insert_front();
    run_linked_list_get();
    run_linked_list_insert_front();
    return 0;
}
