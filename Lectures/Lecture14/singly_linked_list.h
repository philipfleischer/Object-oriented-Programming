/**
 * A node in a singly linked list.
 *
 * Not intended for direct usage, but used by the SinglyLinkedList class.
 */

struct Node
{
    /// @brief An element in th elist (default: most neg int)
    int value = -2147483647;

    /// @brief Pointer to the next node in the list (default: none)
    Node *next = nullptr;
};

/**
 * A singly linked list that also supports indexing
 */
class SinglyLinkedList
{
private:
    /// @internal Pointer to the first node in the list
    Node *_head;

    /**
     * @internal Tracks the number of elements in the lsit.
     * @see length
     */
    int _size;

public:
    /// @brief Creates an empty list with no elements
    SinglyLinkedList();
    ~SinglyLinkedList();

    /**
     * Adds a new value at the end of the list.
     * @param value The integer value of the element.
     */
    void append(int value);

    /// @return The number of elements in the list.
    int length();

    /**
     * Supports the indexing operator: a_list[index]
     * @param index Zero-based index (0 = first element, 1 = second element...)
     * @return A reference to the element at that position if it exists.
     * @throws std::range_error Thrown if the index is outside the list,
     *             or if it is negative
     */
    int &operator[](int index);
};
