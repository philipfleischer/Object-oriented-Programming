/** @file test_array_list.cpp
 *  @brief Unit tests for the dynamic array list (ArrayList).
 *  @details Verifies construction, append, indexing (read/write), insert/remove, pop(index) and pop(), shrink-to-fit behavior, argmin/argmax, min/max, count, and print formatting.
 */
#include <cassert>
#include <iostream>

#include "array_list.h"

/// @brief Test that a newly constructed ArrayList object has length zero.
void test_empty_array_has_length_zero()
{
    ArrayList a = ArrayList();
    std::cout << "Test that empty array has length zero\n";
    assert(a.length() == 0);
    std::cout << " - Success: test_empty_array_has_length_zero()\n"
              << std::endl;
    ;
}

/// @brief Test that appending two elements results in length==2.
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

/// @brief Test to see if operator[] method supports reading and writing for mutable elements.
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

/// @brief Test constructing from std::vector preserves order and length.
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

/// @brief Test insert at front, middle, and end for the ArrayList object.
void test_insert()
{
    std::cout << "Test insert at front, middle, and end.\n";
    ArrayList a = ArrayList({0, 1});
    assert(a.length() == 2);

    a.insert(42, 0); // front/head
    assert(a.length() == 3);
    assert(a[0] == 42);
    assert(a[1] == 0);
    assert(a[2] == 1);

    a.insert(43, 1); // middle
    assert(a.length() == 4);
    assert(a[0] == 42);
    assert(a[1] == 43);
    assert(a[2] == 0);
    assert(a[3] == 1);

    a.insert(44, 4); // end/tail
    assert(a.length() == 5);
    assert(a[0] == 42);
    assert(a[1] == 43);
    assert(a[2] == 0);
    assert(a[3] == 1);
    assert(a[4] == 44);

    std::cout << " - Success: test_insert()\n"
              << std::endl;
}

/// @brief Test that remove() funciton deletes element at the index and shifts elements left.
void test_remove()
{
    std::cout << "Test remove by index.\n";
    ArrayList a({10, 20, 30, 40});
    assert(a.length() == 4);

    // Remove middle element in list
    a.remove(1); // Should remove 20
    assert(a.length() == 3);
    assert(a[0] == 10);
    assert(a[1] == 30);
    assert(a[2] == 40);

    // Remove front element in list
    a.remove(0); // Should remove 10
    assert(a.length() == 2);
    assert(a[0] == 30);
    assert(a[1] == 40);

    // Remove last element in list
    a.remove(1); // Should remove 40
    assert(a.length() == 1);
    assert(a[0] == 30);

    std::cout << "- Success: test_remove()\n"
              << std::endl;
}

/// @brief Test pop(index) returns the removed element and shifts elements.
void test_pop_at_index()
{
    std::cout << "Test pop(index) returns removed element.\n";
    ArrayList a({5, 6, 7, 8});
    assert(a.length() == 4);

    int v = a.pop(2); // Should remove element 7
    assert(v == 7);
    assert(a.length() == 3);
    assert(a[0] == 5);
    assert(a[1] == 6);
    assert(a[2] == 8);

    // pop from front of array
    v = a.pop(0);
    assert(v == 5);
    assert(a.length() == 2);
    assert(a[0] == 6);
    assert(a[1] == 8);

    std::cout << "- Success: test_pop_at_index()\n"
              << std::endl;
}

/// @brief Test pop() removes and returns the last element; throws range_error on empty list operations.
void test_pop()
{
    std::cout << "Test pop() removes last and returns it.\n";
    ArrayList a({1, 2, 3});
    assert(a.length() == 3);

    int v = a.pop();
    assert(v == 3);
    assert(a.length() == 2);

    v = a.pop();
    assert(v == 2);
    assert(a.length() == 1);

    v = a.pop();
    assert(v == 1);
    assert(a.length() == 0);

    // popping from an empty list should throw range_error
    bool threw = false;
    try
    {
        a.pop();
    }
    catch (const std::range_error &)
    {
        threw = true;
    }
    assert(threw && "pop() on empty should throw");

    std::cout << "- Success: test_pop()\n"
              << std::endl;
}

/// @brief Test that print() funciton prints in a nice and correct format.
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

/// @brief Test that capacity shrinks to a small power-of-two after removals result in usage<25%.
void test_shrink_to_fit()
{
    std::cout << "Test shrinking capacity to fit elements.\n";
    // Starting with initializing a large list:
    ArrayList a;
    for (int i = 0; i < 100; i++)
        a.append(i);

    // Pop elements to force shrink_to_fit funciton
    for (int i = 0; i < 90; i++)
        a.pop();

    assert(a.length() == 10);
    // a._shrink_to_fit();
    // Capacity should be 32 now
    assert(a.capacity() == 32);
    std::cout << "- Success: test_shrink_to_fit()\n"
              << std::endl;
}

/// @brief Test argmin returns index of the first minimum element in ArrayList.
void test_argmin()
{
    std::cout << "Test argmin.\n";
    ArrayList a({5, -2, 7, -2, 3});
    // Should find that the first smallest occurrence is on index 1
    assert(a.argmin() == 1);
    std::cout << "- Success: test_argmin()\n"
              << std::endl;
}

/// @brief Test argmax returns index of the first maximum element in ArrayList.
void test_argmax()
{
    std::cout << "Test argmax.\n";
    ArrayList a({5, 42, 7, 42, 3});
    // Should find that the first largest occurrence is on index 1
    assert(a.argmax() == 1);
    std::cout << "- Success: test_argmax()\n"
              << std::endl;
}

/// @brief Test min returns the smallest value in the ArrayList object.
void test_min()
{
    std::cout << "Test min.\n";
    ArrayList a({5, -2, 7, -2, 3});
    // Should find that the smallest element is -2
    assert(a.min() == -2);
    std::cout << "- Success: test_min()\n"
              << std::endl;
}

/// @brief Test max returns the largest value in the ArrayList object.
void test_max()
{
    std::cout << "Test max.\n";
    ArrayList a({5, 42, 7, 42, 3});
    // Should find that the largest element is 42
    assert(a.max() == 42);
    std::cout << "- Success: test_max()\n"
              << std::endl;
}

/// @brief Test count returns the number of occurrences of a value in the ArrayList object.
void test_count()
{
    std::cout << "Test count.\n";
    ArrayList a({1, 2, 2, 3, 2, 4, 2});
    assert(a.count(2) == 4);
    assert(a.count(5) == 0);
    std::cout << "- Success: test_count()\n"
              << std::endl;
}

/// @brief Test that out-of-bounds access and invalid operations throw range_error.
void test_out_of_bounds_exceptions()
{
    std::cout << "Test out-of-bounds exceptions.\n";

    ArrayList a({10, 20, 30});

    // operator[] out of range
    bool threw_index = false;
    try
    {
        int x = a[5];
        (void)x;
    }
    catch (const std::range_error &)
    {
        threw_index = true;
    }
    assert(threw_index && "operator[] should throw on invalid index");

    // insert with bad index
    bool threw_insert = false;
    try
    {
        a.insert(999, -1);
    }
    catch (const std::range_error &)
    {
        threw_insert = true;
    }
    assert(threw_insert && "insert() should throw on invalid index");

    // remove with bad index
    bool threw_remove = false;
    try
    {
        a.remove(10);
    }
    catch (const std::range_error &)
    {
        threw_remove = true;
    }
    assert(threw_remove && "remove() should throw on invalid index");

    // pop(index) with bad index
    bool threw_pop_index = false;
    try
    {
        a.pop(100);
    }
    catch (const std::range_error &)
    {
        threw_pop_index = true;
    }
    assert(threw_pop_index && "pop(index) should throw on invalid index");

    std::cout << "- Success: test_out_of_bounds_exceptions()\n"
              << std::endl;
}

/// @brief Test that capacity actually grows when we append lots of elements.
void test_capacity_grows()
{
    std::cout << "Test capacity grows on append.\n";

    ArrayList a;
    int initial_capacity = a.capacity();
    assert(initial_capacity >= 1);

    // Append enough elements to force at least one resize
    for (int i = 0; i < 100; i++)
        a.append(i);

    assert(a.length() == 100);
    // After appending 100 elements, capacity should be >= length
    assert(a.capacity() >= a.length());
    // And capacity should have increased from the initial capacity
    assert(a.capacity() > initial_capacity);

    std::cout << "- Success: test_capacity_grows()\n"
              << std::endl;
}

/// @brief Runs all ArrayList unit tests in this file.
int main()
{
    test_empty_array_has_length_zero();
    test_array_with_two_elements_appended_has_length_two();
    test_print();
    test_indexing_operator();
    test_vector_constructor();
    test_insert();
    test_remove();
    test_pop_at_index();
    test_pop();
    test_shrink_to_fit();
    test_argmin();
    test_argmax();
    test_min();
    test_max();
    test_count();
    test_out_of_bounds_exceptions();
    test_capacity_grows();
    std::cout << "All tests passed.\n";
    return 0;
}
