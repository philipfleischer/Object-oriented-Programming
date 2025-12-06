#include <iostream>
#include <stdexcept>
#include <vector>

/**
 * @class ArrayList
 * @brief A dynamic array-based list that grows automatically as elements are added.
 *
 * The ArrayList stores integers and uses a fixed-size underlying array. When capacity is reached, the internal array is resized using a growth factor. It supports indexing, element retrieval, and printing.
 */
class ArrayList
{
private:
  /// @internal Array containing the actual data in the list
  int *_data;
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

  /**
   * @brief Shrinks th einternal storage of the arraylist to the smalles power of 2 that can fit all the elements currently in the list.
   *
   * For example: if _size = 47 and _capacity = 1024, shrink_to_fit will set _capacity = 64.
   */
  void _shrink_to_fit();

public:
  /// @brief Constructs an empty ArrayList with an initial capacity of 1
  ArrayList();
  /**
   * @brief Constructs an ArrayList from a vector of integers.
   * @param init A vector used to initialize the array list.
   */
  ArrayList(const std::vector<int> &init);
  /// @brief Destroys the ArrayList object and frees the dynamically allocated internal array.
  ~ArrayList();

  /// @return Length of ArrayList object.
  int length();

  /// @brief Get the current capacity of list.
  int capacity();

  /**
   * @brief Returns a reference to the element at a given index.
   *
   * The function allows for both reading and writing to the mutable element.
   * Throws: std::range_error if the index is out of bounds.
   *
   * @param index The index to access the ArrayList object.
   * @return A reference to the integer at the given index.
   */
  int &operator[](int);

  /**
   * @brief Inserts a value val at the index index in the list.
   *
   * The function shifts the elements at the index and all after the index one position to the right.
   * Inserting at index == length() is allowed (same as append() funciton).
   * Throws std::range_error if index > length().
   *
   * @param val The value to insert in the ArrayList object.
   * @param index The position in the ArrayList object to insert at.
   */
  void insert(int val, int index);

  /**
   * @brief Remove element at index.
   * @throws std::range_error if index is out of bounds.
   */
  void remove(int index);

  /**
   * @brief Appends a new element to the end of the ArrayList.
   *
   * If the internal array is full, it is automatically resized.
   *
   * @param element An integer to be appended.
   */
  void append(int element);

  /**
   * @brief prints the contents of the list to standard output.
   *
   * Print-Format: ArrayList([a, b, c]).
   */
  void print();

  /**
   * @brief Remove and return element at index.
   * @throws std::range_error if index is out of bounds.
   */
  int pop(int);

  /**
   * @brief Remove and return the last element.
   * @throws std::range_error if the ArrayList list object is empty.
   */
  int pop();

  /**
   * @brief Returns the index of the smallest element in the array.
   * @throws std::runtime_error if the list is empty.
   */
  int argmin();

  /**
   * @brief Returns the index of the largest element in the array.
   * @throws std::runtime_error if the list is empty.
   */
  int argmax();

  /**
   * @brief Returns the smallest element in the array.
   * @throws std::runtime_error if the list is empty.
   */
  int min();

  /**
   * @brief Returns the largest element in the array.
   * @throws std::runtime_error if the list is empty.
   */
  int max();

  /**
   * @brief Returns the number of times a given element occurs in the array.
   * @param value Value to be counted in the array.
   * @return Returns number of occurences.
   */
  int count(int);
};
