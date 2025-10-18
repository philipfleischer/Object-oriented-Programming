#include <cassert>
#include <iostream>

#include "array_list.h"

void test_empty_array_has_length_zero()
{
    ArrayList a = ArrayList();
    std::cout << "Test that empty array has length zero\n";
    assert(a.length() == 0);
    std::cout << " - Success: test_empty_array_has_length_zero()\n"
              << std::endl;
    ;
}

void test_array_with_two_elements_appended_has_length_two()
{
    ArrayList a = ArrayList();
    std::cout << "Test that an array list with two elements has length 2.\n";
    a.append(42);
    a.append(-1337);
    assert(a.length() == 2);
    std::cout << " - Success: test_array_with_two_elements_appended_has_length_two()\n"
              << std::endl;
}

void test_print()
{
    std::cout << "Test print.\n";
    ArrayList a;
    a.append(12);
    a.append(2);
    a.append(4);
    a.print();
    std::cout << " - Success: test_print()\n"
              << std::endl;
}

void test_indexing_operator()
{
    std::cout << "Test indexing operator.\n";
    ArrayList a;
    a.append(99);
    a.append(-55);
    a[1] = 1234;
    assert(a[0] == 99);
    assert(a[1] == 1234);
    std::cout << " - Success: test_indexing_operator()\n"
              << std::endl;
}

void test_vector_constructor()
{
    std::cout << "Testing vector constructor.\n";
    ArrayList primes({2, 3, 5, 7, 11});
    assert(primes.length() == 5);
    assert(primes[0] == 2);
    assert(primes[4] == 11);
    primes.print();
    std::cout << " - Success: test_vector_constructor()\n"
              << std::endl;
}

void test_insert()
{
    std::cout << "Test insert at front, middle, and end.\n";
    ArrayList a = ArrayList({0, 1});
    assert(a.length() == 2);

    a.insert(42, 0);
    assert(a.length() == 3);
    assert(a[0] == 42);
    assert(a[1] == 0);
    assert(a[2] == 1);

    a.insert(43, 1);
    assert(a.length() == 4);
    assert(a[0] == 42);
    assert(a[1] == 43);
    assert(a[2] == 0);
    assert(a[3] == 1);

    a.insert(44, 4);
    assert(a.length() == 5);
    assert(a[0] == 42);
    assert(a[1] == 43);
    assert(a[2] == 0);
    assert(a[3] == 1);
    assert(a[4] == 44);

    std::cout << " - Success: test_insert()\n"
              << std::endl;
}

int main()
{
    test_empty_array_has_length_zero();
    test_array_with_two_elements_appended_has_length_two();
    test_print();
    test_indexing_operator();
    test_vector_constructor();
    test_insert();
    std::cout << "All tests passed.\n";
    return 0;
}
