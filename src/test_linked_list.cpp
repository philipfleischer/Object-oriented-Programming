/** @file test_linked_list.cpp
 *  @brief Unit tests for the doubly linked list (LinkedList).
 *  @details Verifies construction from empty list and vector, push_front, append, printing, indexing (read/write), insert at front/middle/end, remove, pop(index), pop() and min/max utilities.
 */
#include <cassert>
#include <iostream>

#include "linked_list.h"

/// @brief Test that a newly constructed LinkedList object has length zero.
void test_empty_list_has_zero_length()
{
    LinkedList dll = LinkedList();
    std::cout << "Test that empty list has length zero";
    assert(dll.length() == 0);
    std::cout << " - Success!" << std::endl;
    ;
}

/// @brief Test that push_front inserts at the head and preserves the order [1,2,3].
void test_push_front()
{
    std::cout << "Test push_front.\n";
    LinkedList dll;
    dll.push_front(3);
    dll.push_front(2);
    dll.push_front(1);
    assert(dll.length() == 3);

    std::cout << "- Expected: \n[1, 2, 3]\nResult: "
              << std::endl;
    dll.print();
    std::cout << "- Success: test_push_front()\n"
              << std::endl;
}

/// @brief Test that append adds element to the tail and updates length and values.
void test_append()
{
    LinkedList dll;
    dll.append(10);
    dll.append(20);
    std::cout << "Test append -> length==2\n";
    assert(dll.length() == 2);
    assert(dll[0] == 10);
    assert(dll[1] == 20);
    std::cout << " - Success: test_append()\n"
              << std::endl;
}

/// @brief Test that print outputs in a nice format.
void test_print()
{
    std::cout << "Test print.\n";
    LinkedList dll;
    dll.append(1);
    dll.append(2);
    dll.append(3);

    std::cout << "- Expected:\n[1, 2, 3]\nResult:\n";
    dll.print();
    std::cout << "- Success: test_print()\n";
}

/// @brief Test operator[] for read and write access to elements in the LinkedList object.
void test_index_operator()
{
    LinkedList dll;
    dll.append(1);
    dll.append(2);
    dll.append(3);
    std::cout << "Test index operator (read/write)\n";
    assert(dll[0] == 1);
    assert(dll[1] == 2);
    assert(dll[2] == 3);
    dll[1] = 42;
    assert(dll[1] == 42);
    std::cout << " - Success: test_index_operator()\n"
              << std::endl;
}

/// @brief Test insert at front, middle, and end for the LinkedList object.
void test_insert()
{
    LinkedList dll;
    dll.append(0);
    dll.append(2);
    dll.append(3);

    // front insertions test
    dll.insert(9, 0);
    // middle insertions test
    dll.insert(1, 2);
    // end insertion/append test
    dll.insert(4, dll.length());

    std::cout << "Test insert (front, middle, end)\n";
    assert(dll.length() == 6);
    assert(dll[0] == 9);
    assert(dll[1] == 0);
    assert(dll[2] == 1);
    assert(dll[3] == 2);
    assert(dll[4] == 3);
    assert(dll[5] == 4);
    std::cout << " - Success: test_insert()\n"
              << std::endl;
}

/// @brief Test construction from std::vector preserves order and length for the LinkedList object.
void test_vector_constructor()
{
    std::cout << "Test vector constructor\n";
    LinkedList primes({2, 3, 5, 7, 11});
    assert(primes.length() == 5);
    assert(primes[0] == 2);
    assert(primes[4] == 11);
    std::cout << " - Success: test_vector_constructor()\n"
              << std::endl;
}

/// @brief Test_remove deletes the element at a given index and compacts links for the LinkedList object.
void test_remove()
{
    std::cout << "Test remove\n";
    LinkedList ll({10, 20, 30, 40});
    ll.remove(1);
    assert(ll.length() == 3);
    assert(ll[0] == 10);
    assert(ll[1] == 30);
    assert(ll[2] == 40);
    std::cout << " - Success: test_remove()\n"
              << std::endl;
}

/// @brief Test pop(int) returns the removed value and updates list structure.
void test_pop_at_index()
{
    std::cout << "Test pop at index\n";
    LinkedList ll({1, 2, 3});
    int val = ll.pop(1);
    assert(val == 2);
    assert(ll.length() == 2);
    assert(ll[0] == 1);
    assert(ll[1] == 3);
    std::cout << " - Success: test_pop_at_index()\n"
              << std::endl;
}

/// @brief Test pop() removes and returns the last element.
void test_pop()
{
    std::cout << "Test pop last element\n";
    LinkedList ll({5, 6, 7});
    int val = ll.pop();
    assert(val == 7);
    assert(ll.length() == 2);
    assert(ll[0] == 5);
    assert(ll[1] == 6);
    std::cout << " - Success: test_pop()\n"
              << std::endl;
}

/// @brief Test min() returns the smallest value in the list.
void test_min()
{
    std::cout << "Test min\n";
    LinkedList ll({5, 2, 9, 1, 7});
    assert(ll.min() == 1);
    std::cout << " - Success: test_min()\n"
              << std::endl;
}

/// @brief Test max() returns the largest value in the list.
void test_max()
{
    std::cout << "Test max\n";
    LinkedList ll({5, 2, 9, 1, 7});
    assert(ll.max() == 9);
    std::cout << " - Success: test_max()\n"
              << std::endl;
}

/// @brief Main function runs all LinkedList unit tests in this file.
int main()
{
    test_empty_list_has_zero_length();
    test_push_front();
    test_append();
    test_print();
    test_index_operator();
    test_insert();
    test_vector_constructor();
    test_remove();
    test_pop_at_index();
    test_pop();
    test_min();
    test_max();
    std::cout << "All Doubly Linked List tests passed.\n";
    return 0;
}
