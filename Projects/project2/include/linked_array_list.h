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
    std::unique_ptr<ArrayList> value; // The unique pointer where we store the ArrayList object
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

/**
 * @brief A doubly linked list class, where each node holds an ArrayList object.
 *
 * @details
 * This class behaves similarly to LinkedList, but each element in the list is an instance of the datastructure ArrayList.
 */
class LinkedArrayList
{
private:
    ArrayListNode *_head; // Pointer to the first node (nullptr if empty).
    ArrayListNode *_tail; // Pointer to the last node (nullptr if empty).
    int _size;            // Number of nodes in the list.

    /**
     * @brief This is a helper method that returns a pointer to the node at the index given.
     * It traverses from the head pointer or tail pointer, depending on which is optimal.
     *
     * @param index The index of the node.
     * @return Returns a pointer to the ArrayListNode object at the index.
     * @throws std::range_error when index is out of bounds.
     */
    ArrayListNode *_node_at(int index);

public:
    /// @brief Constructor for LinkedArrayList objcet.
    LinkedArrayList();

    /// @brief Destructor for LinkedArrayList object that releases all the nodes from memory.
    ~LinkedArrayList();

    /**
     * @brief Appends a new node with an ArrayList containing the given values.
     *
     * @param values A vector of integers to initialize the new ArrayList object.
     */
    void append(std::vector<int> values);

    /**
     * @brief Prints the entire LinkedArrayList structure.
     *
     * Output format for print:
     * [
     *  [1, 2]
     *  [4, 5, 6]
     * ]
     */
    void print();

    /**
     * @brief This enters the ArrayList object at the node index given as an argument.
     *
     * @param index The index of the node to access.
     * @return A reference to the unique_ptr<ArrayList> object contained in the node.
     * @throws std::range_error if index is out of bounds.
     */
    std::unique_ptr<ArrayList> &operator[](int index);

    /// @return Return the number of nodes in the list.
    int length() const { return _size; }
};
