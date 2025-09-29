#include <iostream>
#include <stdexcept>
#include "linked_list.h"

void LinkedList::_check_index_out_of_bounds(int index)
{
    if ((index < 0) || (index >= length()))
        throw std::range_error("Index out of bounds");
}

// Default constructor
LinkedList::LinkedList()
{
    _head = nullptr;
    _size = 0;
}

// Destructor
LinkedList::~LinkedList()
{
    Node* current = _head;
    Node* next = nullptr;
    // Move node until we are at the last element
    while (current != nullptr)
    {
        next = current->next;
        delete current;
        current = next;
    }
}

void LinkedList::print()
{
    std::cout << "[";
    if (_head != nullptr)
    {
        Node* current = _head;
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

int LinkedList::length()
{
    return _size;
}

void LinkedList::push_front(int val)
{
    Node* old_head = _head;
    _head = new Node();
    _head->value = val;
    _head->next = old_head;
    _size++;
}
