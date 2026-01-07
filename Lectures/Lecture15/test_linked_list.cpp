#include <cassert>
#include <iostream>

#include "linked_list.cpp"

void test_empty_list_has_zero_length()
{
    LinkedList ll = LinkedList();
    std::cout << "Test that empty list has length zero";
    assert(ll.length() == 0);
    std::cout << " - Success!" << std::endl;;
}

int main()
{
    test_empty_list_has_zero_length();
    return 0;
}