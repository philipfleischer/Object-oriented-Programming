/**
 * A node in a singly linked list.
 * 
 * Not intended for direct use, but used my the LinkedList class.
 * @see LinkedList
 */
struct Node
{
    /// Value of an element in the list (default: most negative 32-bit int)
    int value = -2147483647;

    /// Pointer to the next element in the list (default: null pointer)
    Node* next = nullptr;
};

/**
 * A singly linked list that supports indexing.
 */
class LinkedList
{
    private:
        /// @internal Pointer to the first element in the list
        Node* _head;

        /**
         * @internal Tracks the number of elements in the list
         * @see length
         */ 
        int _size;

        /**
         * Check wheter the given index if out of
         * bound and throw a range error if it is
         *
         * @param index The index to be checked
         * @throws std::range_error Thrown if the index is negative or
         *         outside the list
         */
        void _check_index_out_of_bounds(int index);

    public:
        LinkedList();
        ~LinkedList();

        /**
         * Adds a new integer element to the end of the list.
         * 
         * @param val The value of the element
         */
        void append(int val);

        /// @return The number of elements in the list
        int length();

        /**
         * Print values in the list
         */
        void print();

        /**
         * Add element to the beginning of the list
         *
         * @param val The value to be added
         */
        void push_front(int val);
};