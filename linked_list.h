#pragma once
#include <iostream>
#include <stdexcept>
#include <vector>

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
    int value = 0;

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
 * @brief A doubly linked list.
 *
 * @details
 * Supports push to front, append to back, printing, and length queries.
 * The list maintains pointers to both head and tail to make front/back operations efficient.
 *
 * @invariant
 *  - (_size == 0) - (_head == nullptr && _tail == nullptr)
 *  - (_size > 0) - (_head != nullptr && _tail != nullptr)
 *  - (_size == 1) - (_head == _tail)
 *  - For any list not empty: _head->prev == nullptr and _tail->next == nullptr
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
     * Check whether the given index is out of bounds and throw a range error if it is.
     *
     * @param index The index to be checked
     * @throws std::range_error Thrown if the index is negative or
     *         outside the list
     */
    void _check_index_out_of_bounds(int index);

    /**
     * @brief Returns a pointer to the node at the index.
     *
     * Used internally to access the node corresponding to an index.
     * Traversing from head or tail, depending on which is the closest one, this is done to reduce the average time complexity.
     *
     * @param index The index of the node to be retrieved.
     * @return A pointer to the node at the given index.
     */
    Node *_node_at(int index);

public:
    /**
     * @brief Constructs an empty list.
     *
     * @post length == 0, _head == nullptr, _tail == nullptr.
     */
    LinkedList();

    /**
     * @brief Constructs a LinkedList object and initializes it with elements from the integer values vector.
     *
     * Each element in the vector gets appended to the dll in order, thereby preserving the order of inserts.
     *
     * @param value A std::vector containing the initial values for the list.
     *
     * @note If the vector is empty, the constructed list will also be empty.
     */
    LinkedList(const std::vector<int> &values);

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

    /**
     * @brief Accesses the element at the specified index in the list.
     *
     * Provides both read and write functionality to telements using the brackets. Operation running in linear time complexity, O(n) in worst case if we need to traverse through the whole list from head to tail.
     *
     * @param index The position of the element to access.
     * @return A reference to the element at the given index.
     *
     * @throws std::range_error if the index is out of bounds.
     */
    int &operator[](int index);

    /**
     * @brief Inserts a value at a specific index in the list.
     *
     * The element at the given index and all elements to the to its right will be shifted one position forward. Insertion at head is the same as push_front() and insertion at tail is the same as append().
     *
     * @param value The value to insert into the linked list.
     * @param index The position to insert the value.
     *
     * @throws std::range_error if the index is out of range.
     *
     * @note The function has linear time complexity in the worst case, O(n).
     */
    void insert(int value, int index);

    /**
     * @brief Removes the element at the given position index.
     * @param index The index of the element to remove.
     * @throws std::range_error if index is out of bounds.
     */
    void remove(int index);

    /**
     * @brief Remove and return the element at the given index.
     * @param index The index of the element to pop.
     * @return The value of the removed element.
     * @throws std::range_error if the list is empty.
     */
    int pop(int index);

    /**
     * @brief Remove and return the element at the end of the list.
     * @return The value of the removed element.
     * @throws std::range_error if the list is empty.
     */
    int pop();

    /**
     * @brief Return the smallest element in the list.
     * @return The smallest element value.
     * @throws std::range_error if the list is empty.
     */
    int min();

    /**
     * @brief Return the largest element in the list.
     * @return The largest element value.
     * @throws std::range_error if the list is empty.
     */
    int max();
};
