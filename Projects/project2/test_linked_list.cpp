#include <cassert>
#include <iostream>

#include "linked_list.h"

void test_empty_list_has_zero_length()
{
    LinkedList ll = LinkedList();
    std::cout << "Test that empty list has length zero";
    assert(ll.length() == 0);
    std::cout << " - Success!" << std::endl;
    ;
}

void test_push_front()
{
    std::cout << "Test push_front.\n";
    LinkedList ll;
    ll.push_front(3);
    ll.push_front(2);
    ll.push_front(1);
    assert(ll.length() == 3);

    std::cout << "- Expected: \n[1, 2, 3]\nResult: "
              << std::endl;
    ll.print();
    std::cout << "- Success: test_push_front()\n"
              << std::endl;
}

int main()
{
    test_empty_list_has_zero_length();
    test_push_front();
    return 0;
}
