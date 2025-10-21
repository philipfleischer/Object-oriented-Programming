#include "linked_array_list.h"
#include <assert.h>

void test_array_list_node()
{
    std::cout << "--- Testing ArrayListNode\n";

    // Initializing three nodes
    ArrayListNode node1({1, 2, 3}, nullptr, nullptr);
    ArrayListNode node2({4, 5}, &node1, nullptr);
    ArrayListNode node3({9}, &node2, nullptr);

    // Linking the next pointers
    node1.next = &node2;
    node2.next = &node3;

    // Printing the states
    std::cout << "Initial node values:\n";
    node1.val->print(); // [1, 2, 3]
    node2.val->print(); // [4, 5]
    node3.val->print(); // [9]

    // Using functions
    node2.val->append(6);
    node2.val->insert(0, 0);

    std::cout << "\nAfter modifying node2:\n";
    node2.val->print(); // Expect output to be: [0, 4, 5, 6]
    node1.val->print(); // Expect output to be:[1, 2, 3]
    node3.val->print(); // Expect output to be: [9]

    // Traversing using next-pointers (i.e.: forward in list)
    std::cout << "\nForward traversal:\n";
    ArrayListNode *forward = &node1;
    while (forward != nullptr)
    {
        forward->val->print();
        forward = forward->next;
    }

    // Traversing using prev-pointers (i.e.: backwards in list)
    std::cout << "\nBackward traversal:\n";
    ArrayListNode *backward = &node3;
    while (backward != nullptr)
    {
        backward->val->print();
        backward = backward->prev;
    }

    // Assertions to check if logic is correct
    assert(node1.next == &node2);
    assert(node2.prev == &node1);
    assert(node2.next == &node3);
    assert(node3.prev == &node2);
    assert(node2.val->length() == 4);
    assert(node1.val->length() == 3);

    std::cout << "\n--- All ArrayListNode tests passed.\n";
}

int main()
{
    test_array_list_node();
    return 0;
}
