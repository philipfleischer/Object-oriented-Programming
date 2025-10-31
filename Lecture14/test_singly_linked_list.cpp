#include <cassert>
#include <iostream>

#include "singly_linked_list.h"

void test_append_and_get()
{
    SinglyLinkedList sll = SinglyLinkedList();
    sll.append(8);
    sll.append(64);
    assert(sll[0] == 8);
    assert(sll[1] == 64);

    std::cout << "test_append_and_get() OK" << std::endl;
}

void test_access_element_out_of_bounce_throws_range_error()
{
    SinglyLinkedList sll = SinglyLinkedList();
    bool range_error_thrown = false;

    try
    {
        int x = sll[0];
    }
    catch (const std::range_error &e)
    {
        range_error_thrown = true;
    }

    std::cout << "test_access_element_out_of_bounce_throws_range_error() OK" << std::endl;
}

int main()
{
    test_append_and_get();
}
