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

// Return pointer to node at index (0.._size-1). Assumes index is valid.
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

int &LinkedList::operator[](int index)
{
    _check_index_out_of_bounds(index);
    return _node_at(index)->value;
}

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

LinkedList::LinkedList(const std::vector<int> &values)
    : _head(nullptr), _tail(nullptr), _size(0)
{
    for (int value : values)
        append(value);
}
