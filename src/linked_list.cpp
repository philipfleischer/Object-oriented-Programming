// linked_list.cpp

#include <iostream>
#include <stdexcept>
#include "linked_list.h"

/**
 * @brief Validate that an index is within bounds
 * @param index Index to check.
 * @throws std::range_error if @p index is out of bounds.
 * @note Private helper, called by methods that access elements by indexes.
 */
void LinkedList::_check_index_out_of_bounds(int index)
{
    if ((index < 0) || (index >= length()))
        throw std::range_error("Index out of bounds");
}

/**
* @brief Return a pointer to the node at the given index (0.._size-1).
* @param index Valid index; the caller must ensure bounds are checked.
* @return Pointer to the node at @p index.
* @note Chooses direction from head or tail to reduce traversal steps.
*/
Node *LinkedList::_node_at(int index)
{
    // Choose shortest direction
    if (index <= _size / 2)
    {
        Node *current_node = _head;
        for (int i = 0; i < index; i++)
            current_node = current_node->next;
        return current_node;
    }
    else
    {
        Node *current_node = _tail;
        for (int i = _size - 1; i > index; i--)
            current_node = current_node->prev;

        return current_node;
    }
}

/**
 * @brief Constructs an empty LinkedList
 * @note Sets head and tail to nullptr and size to 0.
 */
LinkedList::LinkedList()
{
    _head = nullptr;
    _tail = nullptr;
    _size = 0;
}

/**
 * @brief Destructor: Deletes all nodes and resets the states.
 */
LinkedList::~LinkedList()
{
    Node *current = _head;
    while (current != nullptr)
    {
        Node *next = current->next;
        delete current;
        current = next;
    }
    _head = nullptr;
    _tail = nullptr;
    _size = 0;
}

/**
 * @brief Prints list contents in the format [a0, a1, ..., an].
 */
void LinkedList::print()
{
    std::cout << "[";
    if (_head != nullptr)
    {
        Node *current = _head;
        while (current->next != nullptr)
        {
            std::cout << current->value;
            std::cout << ", ";
            current = current->next;
        }
        std::cout << current->value;
    }
    std::cout << "]" << std::endl;
}

/**
 * @brief Returns the current size of the list.
 */
int LinkedList::length()
{
    return _size;
}

/**
 * @brief Inserts a new value at the front of the list.
 * @param val Value to insert.
 * @note Handles the empty list case by setting the head and tail.
 */
void LinkedList::push_front(int val)
{
    Node *node = new Node();
    node->value = val;
    node->prev = nullptr; // The new head has no prev node
    node->next = _head;   // The previous head becomes next pointer

    if (_head == nullptr)
    {
        // List was empty, meaning head an tail are node
        _head = node;
        _tail = node;
    }
    else
    {
        // Linking previous old head to the new head
        _head->prev = node;
        _head = node;
    }

    _size++;
}

/**
 * @brief Appends a new value at the end of the list.
 * @param val Value to append.
 * @note Handles the empty list case by setting both the head and tail.
 */
void LinkedList::append(int val)
{
    Node *node = new Node();
    node->value = val;
    node->next = nullptr; // Newly created node has no next pointer

    if (_tail == nullptr)
    {
        // List is empty, meaning head and tail are node
        _head = node;
        _tail = node;
    }
    else
    {
        // Linking after the current tail
        node->prev = _tail;
        _tail->next = node;
        _tail = node;
    }

    _size++;
}

/**
* @brief Indexed element access with bounds checking.
* @param index Element index (0.._size-1).
* @return Reference to the value at @p index.
* @throws std::range_error if index is out of bounds.
*/
int &LinkedList::operator[](int index)
{
    _check_index_out_of_bounds(index);
    return _node_at(index)->value;
}

/**
* @brief Insert a value at a specific index, shifting subsequent nodes.
* @param val Value to insert.
* @param index Position at which to insert (0.._size). Inserting at _size appends.
* @throws std::range_error if index is out of bounds.
*/
void LinkedList::insert(int val, int index)
{
    // Allowed range is 0.._size
    if (index < 0 || index > _size)
        throw std::range_error("Insert index out of bounds");

    if (index == 0)
    {
        push_front(val);
        return;
    }

    if (index == _size)
    {
        append(val);
        return;
    }

    // Insert before node at index
    Node *current_node = _node_at(index);
    Node *prev_node = current_node->prev;

    Node *new_node = new Node();
    new_node->value = val;

    new_node->prev = prev_node;
    new_node->next = current_node;
    prev_node->next = new_node;
    current_node->prev = new_node;

    _size++;
}

/**
* @brief Construct a list from an initializer vector, appending values in order.
* @param values Values to append to the list.
*/
LinkedList::LinkedList(const std::vector<int> &values)
    : _head(nullptr), _tail(nullptr), _size(0)
{
    for (int value : values)
        append(value);
}

/**
* @brief Remove the element at a given index.
* @param index Index of the element to remove (0.._size-1).
* @throws std::range_error if index is out of bounds.
*/
void LinkedList::remove(int index)
{
    _check_index_out_of_bounds(index);

    Node *target_node = _node_at(index);

    if (target_node->prev != nullptr)
        target_node->prev->next = target_node->next;
    else
        // Removing the head
        _head = target_node->next;

    if (target_node->next != nullptr)
        target_node->next->prev = target_node->prev;
    else
        // Removing the tail
        _tail = target_node->prev;

    delete target_node;
    _size--;
}

/**
* @brief Remove and return the element at the given index.
* @param index Index of the element to pop (0.._size-1).
* @return The removed value.
* @throws std::range_error if index is out of bounds.
*/
int LinkedList::pop(int index)
{
    _check_index_out_of_bounds(index);
    Node *target_node = _node_at(index);
    int node_value = target_node->value;

    if (target_node->prev != nullptr)
        target_node->prev->next = target_node->next;
    else
        _head = target_node->next;

    if (target_node->next != nullptr)
        target_node->next->prev = target_node->prev;
    else
        _tail = target_node->prev;

    delete target_node;
    _size--;

    return node_value;
}

/**
* @brief Remove and return the last element of the list.
* @return The removed value.
* @throws std::range_error if the list is empty.
*/
int LinkedList::pop()
{
    if (_size == 0)
        throw std::range_error("Cannot pop from empty list.");

    Node *target_node = _tail;
    int node_value = target_node->value;

    if (target_node->prev != nullptr)
    {
        target_node->prev->next = nullptr;
        _tail = target_node->prev;
    }
    else
    {
        _head = nullptr;
        _tail = nullptr;
    }

    delete target_node;
    _size--;

    return node_value;
}

/**
* @brief Compute the minimum element value in the list.
* @return The smallest value.
* @throws std::range_error if the list is empty.
*/
int LinkedList::min()
{
    if (_size == 0)
        throw std::range_error("Cannot get min from empty list");

    Node *current_node = _head;
    int min_value = current_node->value;
    while (current_node != nullptr)
    {
        if (current_node->value < min_value)
            min_value = current_node->value;
        current_node = current_node->next;
    }
    return min_value;
}

/**
* @brief Compute the maximum element value in the list.
* @return The largest value.
* @throws std::range_error if the list is empty.
*/
int LinkedList::max()
{
    if (_size == 0)
        throw std::range_error("Cannot get max from empty list");

    Node *current_node = _head;
    int max_value = current_node->value;
    while (current_node != nullptr)
    {
        if (current_node->value > max_value)
            max_value = current_node->value;
        current_node = current_node->next;
    }
    return max_value;
}
