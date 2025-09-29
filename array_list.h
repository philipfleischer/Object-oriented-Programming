#include <iostream>
#include <stdexcept>

/**
 * An array-based list that shrinks and grows as needed. Supports indexing.
 */ 
class ArrayList
{
  private:
    /// @internal Array containing the actual data in the list
    int* _data;
    /// @internal Capacity of the array
    int _capacity;
    /// @internal Size of the array
    int _size;
    /// @internal Growth factor - multiply capacity by this when full
    int _growth_factor;

    /**
     * @brief Resize array using _growth_factor.
     * Resize the internal array _data when necessary.
     * Copy all data to a larger array, and delete the old array.
     */
    void _resize(); 

  public:
    ArrayList();    // init - constructor
    ~ArrayList();   // free memory used in function

    /// @return Length of array
    int length();

    /**
     * Appends a new element to the end of the ArrayList.
     * 
     * @param element An integer to append.
     */
    void append(int element);

    /**
     * Get value at a given index.
     * Throws a range error in index if out of bounds
     *
     * @param index The index
     * @return int The value at that index
     */
    int get(int index);

    /**
     * Prints the array
     *
     */
    void print();

    /**
     * Get a reference to the value at a given index.
     * Throws a range error in index if out of bounds
     *
     * @param index The index
     * @return int The value at that index
     */
    int& operator[](int index);
};