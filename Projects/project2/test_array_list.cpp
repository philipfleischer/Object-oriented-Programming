#include <cassert>
#include <iostream>

#include "array_list.h"

void test_empty_array_has_length_zero()
{
    ArrayList a = ArrayList();
    std::cout << "Test that empty array has length zero";
    assert(a.length() == 0);
    std::cout << " - Success!" << std::endl;
    ;
}

void test_array_with_two_elements_appended_has_length_two()
{
    ArrayList a = ArrayList();
    std::cout << "Test that an array list with two elements has length 2.";
    a.append(42);
    a.append(-1337);
    assert(a.length() == 2);
    std::cout << " - Success!" << std::endl;
}

void test_print()
{
    std::cout << "Test print.";
    ArrayList a;
    a.append(12);
    a.append(2);
    a.append(4);
    a.print();
}

void test_indexing_operator()
{
    std::cout << "Test indexing operator.";
    ArrayList a;
    a.append(99);
    a.append(-55);
    a[1] = 1234;
    assert(a[0] == 99);
    assert(a[1] == 1234);
    std::cout << " - Success!\n";
}

void test_vector_constructor()
{
    std::cout << "Testing vector constructor.";
    ArrayList primes({2, 3, 5, 7, 11});
    assert(primes.length() == 5);
    assert(primes[0] == 2);
    assert(primes[4] == 11);
    primes.print();
    std::cout << " - Success!\n";
}

int main()
{
    test_empty_array_has_length_zero();
    test_array_with_two_elements_appended_has_length_two();
    test_print();
    test_indexing_operator();
    test_vector_constructor();
    std::cout << "All tests passed.\n";
    return 0;
}
