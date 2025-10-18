#include <cassert>
#include <iostream>

#include "linked_list.h"

void test_empty_list_has_zero_length()
{
    LinkedList dll = LinkedList();
    std::cout << "Test that empty list has length zero";
    assert(dll.length() == 0);
    std::cout << " - Success!" << std::endl;
    ;
}

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

int main()
{
    test_empty_list_has_zero_length();
    test_push_front();
    test_append();
    test_index_operator();
    test_insert();
    test_vector_constructor();
    test_remove();
    test_pop_at_index();
    test_pop();
    std::cout << "All linked list tests passed.\n";
    return 0;
}
