#include <stdexcept>
#include "linked_array_list.h"

/// @brief Constructs an ArrayListNode object and initializes the ArrayList object with the values passed.
ArrayListNode::ArrayListNode(std::vector<int> values,
                             ArrayListNode *prev,
                             ArrayListNode *next)
{
    // Allocating and initializing a new ArrayList object, thereby transferring the ownership of the object to the unique_ptr.
    value = std::make_unique<ArrayList>(values);
    this->prev = prev;
    this->next = next;
}
/// @brief Constructs an empty LinkedArrayList object with currently no nodes.
LinkedArrayList::LinkedArrayList()
{
    this->_head = nullptr;
    this->_tail = nullptr;
    this->_size = 0;
}

/// @brief Destructor that deallocates/frees all the nodes and their subsequent ArrayLists.
LinkedArrayList::~LinkedArrayList()
{
    // Destructor: Deletes all the nodes in the LinkedArrayList object
    ArrayListNode *current_node = _head;
    while (current_node != nullptr)
    {
        ArrayListNode *next = current_node->next;
        delete current_node;
        current_node = next;
    }
    _head = nullptr;
    _tail = nullptr;
    _size = 0;
}

/// @brief Appends a new ArrayListNode at the end of the list with the parameter values.
void LinkedArrayList::append(std::vector<int> values)
{
    ArrayListNode *new_node = new ArrayListNode(values, _tail, nullptr);

    if (_head == nullptr)
    {
        _head = new_node;
        _tail = new_node;
    }
    else
    {
        _tail->next = new_node;
        _tail = new_node;
    }

    _size++;
}

/// @brief Returns a pointer to the node at the index given.
ArrayListNode *LinkedArrayList::_node_at(int index)
{
    if (index < 0 || index >= _size)
        throw std::range_error("Index out of bounds");

    // Traverse from whichever end (head/tail) is closer
    if (index <= _size / 2)
    {
        ArrayListNode *current_node = _head;
        for (int i = 0; i < index; i++)
            current_node = current_node->next;
        return current_node;
    }
    else
    {
        ArrayListNode *current_node = _tail;
        for (int i = _size - 1; i > index; i--)
            current_node = current_node->prev;
        return current_node;
    }
}

/// @brief Returns a reference to the unique_ptr<ArrayList> object stored at the index in the list.
std::unique_ptr<ArrayList> &LinkedArrayList::operator[](int index)
{
    return _node_at(index)->value;
}

/// @brief This prints all the ArrayList object in the LinkedArraList object in a nested list format.
void LinkedArrayList::print()
{
    std::cout << "[\n";
    ArrayListNode *current_node = _head;
    while (current_node != nullptr)
    {
        std::cout << " ";
        current_node->value->print(); // Calling the print() function for ArrayList here
        current_node = current_node->next;
    }
    std::cout << "]\n";
}
