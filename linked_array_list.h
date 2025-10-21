#pragma once
#include <memory>
#include <vector>
#include "array_list.h"

/**
 * @brief Node in a doubly linked structure where each node is an ArrayList.
 *
 * The ArrayList is owned via std::unique_ptr. Nodes are doubly linked using the prev/next pointers.
 */
struct ArrayListNode
{
    std::unique_ptr<ArrayList> val; // The unique pointer where we store the ArrayList object
    ArrayListNode *prev;
    ArrayListNode *next;

    /**
     * @brief Construct a node that has an ArrayList object initialized.
     * @param values Elements used to construct the inner ArrayList.
     * @param prev Pointer to previous node.
     * @param next Pointer to next node.
     */
    ArrayListNode(std::vector<int> values, ArrayListNode *prev, ArrayListNode *next);
};
