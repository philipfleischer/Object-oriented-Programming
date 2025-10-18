#pragma once
#include <iostream>
#include <stdexcept>

/**
 * @brief Node in a doubly linked list.
 *
 * @details
 * Holds an integer value and links to the previous and next nodes.
 * This type is an implementation detail of @ref LinkedList and is not intended for direct use by client code.
 *
 * @see LinkedList
 */
struct Node
{
    /**
     * @brief Stored value for the node.
     *
     * @note Value of an element in the list (default: most negative 32-bit int). Real values are set by the linked list.
     */
    int value = -2147483647;

    /**
     * @brief Pointer to the next node in the list.
     *
     * @note nullptr if this is the tail (or the list is empty).
     */
    Node *next = nullptr;

    /**
     * @brief Pointer to the previous node in the list.
     *
     * @note nullptr if this is the head (or the list is empty).
     */
    Node *prev = nullptr;
};

/**
 * @brief A doubly linmked list.
 *
 * @details
 * Supports push to front, append to back, printing, and length queries.
 * The list maintains pointers to both head and tail to make front/back operations efficient.
 *
 * @invariant
 * - If the list is empty, that means: _head == nullptr && _tail == nullptr && _size == nullptr.
 * - If the list is not empty, then: _head->next != nullptr && _tail->prev != nullptr.
 * - _size is equal to the number of nodes counted from _head->next until it equals nullptr.
 */
class LinkedList
{
private:
    /// @internal Pointer to the first element in the list (head), nullptr on empty
    Node *_head;

    /// @internal Pointer to the last element in the list (tail), nullptr on empty
    Node *_tail;

    /**
     * @internal Tracks the number of elements in the list.
     * @see length().
     */
    int _size;

    /**
     * Check wheter the given index is out of bounds and throw a range error if it is.
     *
     * @param index The index to be checked
     * @throws std::range_error Thrown if the index is negative or
     *         outside the list
     */
    void _check_index_out_of_bounds(int index);

public:
    /**
     * @brief Constructs an empty list.
     *
     * @post length == 0, _head == nullptr, _tail == nullptr.
     */
    LinkedList();

    /**
     * @brief Destroys the list and releases all nodes.
     *
     * @post All dynamically allocated nodes are deleted.
     */
    ~LinkedList();

    /**
     * @brief Appends a value at the end of the list.
     *
     * @param val The value of the element to append.
     * @post length increments by 1 and new value is at index length-1
     */
    void append(int val);

    /// @return The number of elements in the list.
    int length();

    /**
     * @brief Prints the list contents.
     *
     * @details
     * The format is [a0, a1, ..., an].
     */
    void print();

    /**
     * @brief Inserts a value at the front of the list.
     *
     * @param val The value to be pushed at the head.
     * @post length increments by 1 and new value at index 0.
     */
    void push_front(int val);
};
