#include <iostream>
#include <stdexcept>
#include "linked_list.h"

/**
 * @brief throws if index is out of bounds.
 * @note Private helper, called by methods that access elements by indexes.
 */
void LinkedList::_check_index_out_of_bounds(int index)
{
    if ((index < 0) || (index >= length()))
        throw std::range_error("Index out of bounds");
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
 * @brief Destructur: Deletes all nodes and resets the states.
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
 * @brief Prints list contents int the format [a0, a1, ..., an].
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
