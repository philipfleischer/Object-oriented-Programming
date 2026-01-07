#include <cassert>
#include <iostream>

#include "array_list.cpp"
// #include "array_list.h"

void test_empty_array_has_length_zero()
{
    ArrayList a = ArrayList();
    std::cout << "Test that empty array has length zero";
    assert(a.length() == 0);
    std::cout << " - Success!" << std::endl;
    ;
}

void test_array_with_two_elements_has_length_two()
{
    ArrayList a = ArrayList();
    std::cout << "Test that an array list with two elements has length 2.";
    a.append(42);
    a.append(-1337);
    assert(a.length() == 2);
    a.get(1);
    std::cout << " - Success!" << std::endl;
}

int main()
{
    test_empty_array_has_length_zero();
    test_array_with_two_elements_has_length_two();
}
