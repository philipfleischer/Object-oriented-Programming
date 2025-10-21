/** @file test_linked_array_list.cpp
 *  @brief Tests for ArrayListNode and LinkedArrayList.
 *  @details Tests ownership (unique_ptr<ArrayList>), forward/backward traversal with prev/next nodes, LinkedArrayList append, indexing via operator[], and printing nested arrays.
 */
#include <assert.h>
#include "linked_array_list.h"

/// @brief Create a multiple ArrayListNode objects and set links and contents and check if they are reasonable.
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
    node1.value->print(); // [1, 2, 3]
    node2.value->print(); // [4, 5]
    node3.value->print(); // [9]

    // Using functions
    node2.value->append(6);
    node2.value->insert(0, 0);

    std::cout << "\nAfter modifying node2:\n";
    node2.value->print(); // Expect output to be: [0, 4, 5, 6]
    node1.value->print(); // Expect output to be:[1, 2, 3]
    node3.value->print(); // Expect output to be: [9]

    // Traversing using next-pointers (i.e.: forward in list)
    std::cout << "\nForward traversal:\n";
    ArrayListNode *forward = &node1;
    while (forward != nullptr)
    {
        forward->value->print();
        forward = forward->next;
    }

    // Traversing using prev-pointers (i.e.: backwards in list)
    std::cout << "\nBackward traversal:\n";
    ArrayListNode *backward = &node3;
    while (backward != nullptr)
    {
        backward->value->print();
        backward = backward->prev;
    }

    // Assertions to check if logic is correct
    assert(node1.next == &node2);
    assert(node2.prev == &node1);
    assert(node2.next == &node3);
    assert(node3.prev == &node2);
    assert(node2.value->length() == 4);
    assert(node1.value->length() == 3);

    std::cout << "\n--- All ArrayListNode tests passed.\n";
}

/// @brief Test to see the whole datastructure being used.
void test_LinkedArrayList()
{
    LinkedArrayList lal;

    lal.append({1, 2});    // Adding a sublist to the ArrayList object
    lal.append({4, 5, 6}); // Adding asecond sublist
    lal.print();

    lal[0]->append(42);
    lal.print();

    lal[1]->insert(99, 1);
    lal.print();
    std::cout << "\n--- All LinkedArrayList tests passed.\n";
}

/// @brief Runs all LinkedArrayList-related tests in this file.
int main()
{
    test_array_list_node();
    test_LinkedArrayList();
    std::cout << "\n--- All tests for exercise 4 passed.\n";
    return 0;
}
