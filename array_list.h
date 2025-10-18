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

  /**
   * @brief Appends a new element to the end of the ArrayList.
   *
   * If the internal array is full, it is automatically resized.
   *
   * @param element An integer to be appended.
   */
  void append(int element);

  /**
   * @brief Returns value at a given index.
   * Throws a std::range_errorif index out of bounds.
   *
   * @param index The index to access the ArrayList object.
   * @return The value at that index.
   */
  int get(int index);

  /**
   * @brief prints the contents of the list to standard output.
   *
   * Print-Format: ArrayList([a, b, c]).
   */
  void print();

  /**
   * @brief Returns a reference to the element at a given index.
   *
   * The function allows for both reading and writing to the mutable element.
   * Throws: std::range_error if the index is out of bounds.
   *
   * @param index The index to access the ArrayList object.
   * @return A reference to the integer at the given index.
   */
  int &operator[](int index);
  /**
   * @brief Returns a const reference to the element at a given index.
   *
   * Can only be used for reading, not modifying.
   * Throws std::range_error if the index is out of bounds.
   *
   * @param index The index to access in the ArrayList object.
   * @return A const reference to the integer at the given index.
   */
  const int &operator[](int index) const;
};
