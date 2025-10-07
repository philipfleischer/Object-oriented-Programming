#include <stdexcept>

#include "singly_linked_list.h"

// konstruktør
SinglyLinkedList::SinglyLinkedList()
{
    _head = nullptr; // Peker på første node (første element)
    _size = 0;
}

// Destruktør - rydde opp og slette konstruktøren
SinglyLinkedList::SinglyLinkedList()
{
    Node *current_node = _head;
    while (current_node != nullptr) // så lenge det er flere noder...
    {
        Node *next_node = current_node->next; // lagre adresen til neste node.
        delete current_node;                  // Slett noden vi er på (frigjør minne)
        current_node = next_node;             // Gå til neste (hvis den finnes)
    }
}

int SinglyLinkedList::length()
{
    return _size;
}

void SinglyLinkedList::append(int value)
{
    _size++; // Oppfaterer lengedn av listen
    Node *new_node = new Node();
    new_node->value = value;

    // er liste tom?
    if (_head == nullptr)
    {
        _head = new_node;
        return;
    }
    else
    {
        Node *current_node = _head;

        // Gå videre til vi kommer til slutten av listen
        while (current_node->next != nullptr)
        {
            current_node = current_node->next;
        }

        // Nå er current_node den siste som var i listen fra før
        current_node->next = new_node;
    }
}

int &SinglyLinkedList::operator[](int index)
{
    // Gir feilmelding ved ulovlig indeks
    if ((index < 0) || (index >= length()))
    {
        throw std::range_error("Index out of bounds.");
    }

    // TODO: Returner -> value til ritkig node
}
