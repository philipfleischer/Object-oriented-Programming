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

/// @brief Out-of-bounds on operator[] should throw std::range_error.
void test_out_of_bounds_exceptions()
{
    std::cout << "Test out-of-bounds exceptions\n";

    LinkedArrayList lal;
    lal.append({10});
    lal.append({20, 21});

    bool threw_low = false;
    try {
        auto &x = lal[-1]; (void)x;
    } catch (const std::range_error&) { threw_low = true; }
    assert(threw_low && "operator[] should throw on negative index");

    bool threw_high = false;
    try {
        auto &y = lal[5]; (void)y;
    } catch (const std::range_error&) { threw_high = true; }
    assert(threw_high && "operator[] should throw on too-large index");

    std::cout << " - Success: test_out_of_bounds_exceptions()\n\n";
}

/// @brief After multiple appends, head points to first and tail to last.
void test_head_tail_after_appends()
{
    std::cout << "Test head/tail after appends\n";

    LinkedArrayList lal;
    lal.append({1});          // idx 0
    lal.append({2, 3});       // idx 1
    lal.append({4, 5, 6});    // idx 2

    // Check first sublist
    assert((*lal[0])[0] == 1);
    // Check last sublist
    assert((*lal[2])[0] == 4);
    assert(lal[2]->length() == 3);

    // Mutate tail and ensure it's still last and correct
    lal[2]->append(7);
    assert(lal[2]->length() == 4);
    assert((*lal[2])[3] == 7);

    std::cout << " - Success: test_head_tail_after_appends()\n\n";
}

/// @brief Changing one nested ArrayList must not affect others.
void test_mutating_nested_lists_is_local()
{
    std::cout << "Test independence of nested lists\n";

    LinkedArrayList lal;
    lal.append({1, 2});         // idx 0
    lal.append({10, 20, 30});   // idx 1

    // Change only idx 1
    lal[1]->insert(15, 1);      // {10,15,20,30}
    lal[1]->append(40);         // {10,15,20,30,40}

    // Ensure idx 0 stayed the same
    assert(lal[0]->length() == 2);
    assert((*lal[0])[0] == 1);
    assert((*lal[0])[1] == 2);

    // Ensure idx 1 has the new values
    assert(lal[1]->length() == 5);
    assert((*lal[1])[1] == 15);
    assert((*lal[1])[4] == 40);

    std::cout << " - Success: test_mutating_nested_lists_is_local()\n\n";
}

/// @brief Append many sublists and sample a few indices via operator[].
void test_append_many_and_indexing()
{
    std::cout << "Test append many and random indexing\n";

    LinkedArrayList lal;
    for (int i = 0; i < 50; ++i) {
        // each sublist: {i, i+1}
        lal.append({i, i + 1});
    }
    assert((*lal[0])[0] == 0);
    assert((*lal[10])[1] == 11);
    assert((*lal[49])[0] == 49);

    // Mutate a couple of inner lists
    lal[0]->append(99);       // {0,1,99}
    lal[49]->insert(77, 1);   // {49,77,50}

    assert(lal[0]->length() == 3);
    assert((*lal[0])[2] == 99);

    assert(lal[49]->length() == 3);
    assert((*lal[49])[1] == 77);

    std::cout << " - Success: test_append_many_and_indexing()\n\n";
}
/// @brief Runs all LinkedArrayList-related tests in this file.
int main()
{
    test_array_list_node();
    test_LinkedArrayList();
    test_out_of_bounds_exceptions();
    test_head_tail_after_appends();
    test_mutating_nested_lists_is_local();
    test_append_many_and_indexing();
    std::cout << "\n--- All tests passed.\n";
    return 0;
}
