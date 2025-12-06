// array_list.cpp

#include <iostream>
#include <stdexcept>
#include "array_list.h"

/**
* @brief Resize the internal storage to a larger capacity.
*
*/
void ArrayList::_resize()
{
    _capacity *= _growth_factor;

    // New array (pointer), allocating a new larger array
    int *new_data = new int[_capacity];

    // Copy data old --> new array
    for (int i = 0; i < _size; i++)
        new_data[i] = _data[i];

    // Deleting old array - cleaning up after new
    delete[] _data;

    // Using new array hereafter
    _data = new_data;
}

/**
* @brief Reduce capacity to the smallest power of two that can hold the current size.
*
* If the list is empty, capacity becomes 1. Otherwise, compute the smallest power of two
* >= _size, and if it differs from the current capacity, reallocate and copy elements.
*
* @post _capacity may be reduced while preserving all elements.
*/
void ArrayList::_shrink_to_fit()
{
    if (_size == 0)
    {
        // The minimum capacity should be 1 here
        delete[] _data;
        _capacity = 1;
        _data = new int[_capacity];
        return;
    }

    // Finding the smallest power of 2 to contain elements
    int new_capacity = 1;
    while (new_capacity < _size)
        new_capacity *= 2;

    if (new_capacity == _capacity)
        return;

    int *new_data = new int[new_capacity];

    // Copying over the exisiting elements to the new smaller array
    for (int i = 0; i < _size; i++)
        new_data[i] = _data[i];

    delete[] _data;
    _data = new_data;
    _capacity = new_capacity;
}

/**
* @brief Default constructor. Initializes an empty list with capacity 1.
*/
ArrayList::ArrayList()
{
    _capacity = 1;
    _size = 0;
    _data = new int[_capacity];
    _growth_factor = 2;
}

/**
* @brief Construct a list from an initial vector of values.
*
* @param init Initial values to copy into the list.
*
* Capacity is set to at least 1 and at least the number of elements in @p init.
*/
ArrayList::ArrayList(const std::vector<int> &init)
{
    _growth_factor = 2;
    _size = static_cast<int>(init.size());
    _capacity = (_size == 0) ? 1 : _size;
    _data = new int[_capacity];
    for (int i = 0; i < _size; i++)
        _data[i] = init[static_cast<size_t>(i)];
}

/**
* @brief Destructor. Releases allocated memory.
*/
ArrayList::~ArrayList()
{
    delete[] _data;
}

/**
* @brief Get the number of elements currently stored in the list.
* @return Current size (number of elements).
*/
int ArrayList::length()
{
    return _size;
}

/**
* @brief Get the current capacity of the internal array.
* @return Allocated capacity (in number of elements).
*/
int ArrayList::capacity()
{
    return _capacity;
}

/**
* @brief Append an element at the end of the list.
*
* Resizes the internal storage if necessary.
*
* @param element Value to append.
*/
void ArrayList::append(int element)
{
    // Check if array _data need to be resized _resize
    if (_size == _capacity)
        _resize();

    _data[_size] = element;
    _size++;
}

/**
* @brief Insert a value at the given index, shifting subsequent elements right.
*
* @param val Value to insert.
* @param index Position at which to insert (0.._size).
* @throws std::range_error if index is out of bounds.
*/
void ArrayList::insert(int val, int index)
{
    // Allowing insertions at the end of list
    if (index < 0 || index > _size)
        throw std::range_error("Index out of bounds in insertion.\n");

    // We resize the array if necessary
    if (_size == _capacity)
        _resize();

    // Shifting elements to the right
    for (int i = _size; i > index; i--)
        _data[i] = _data[i - 1];

    // Inserting the new value into the array, at the correct now duplicated value position
    _data[index] = val;
    _size++;
}

/**
* @brief Remove the element at the given index, shifting elements left.
*
* @param index Position of the element to remove (0.._size-1).
* @throws std::range_error if index is out of bounds.
*
* If usage drops below 25% of capacity, shrink-to-fit is triggered.
*/
void ArrayList::remove(int index)
{
    if (index < 0 || index >= _size)
        throw std::range_error("Index out of bounds in remove.\n");

    // Removing the element at ArrayList of index, with its right element, doing this until we are at the end of the list
    for (int i = index + 1; i < _size; i++)
        _data[i - 1] = _data[i];
    _size--;

    // Automatically shrinking ArrayList object if it is less than 25% capacity in use
    if (_size < _capacity / 4)
        _shrink_to_fit();
}

/**
* @brief Remove and return the element at the given index.
*
* @param index Position of the element to pop (0.._size-1).
* @return The removed value.
* @throws std::range_error if index is out of bounds.
*/
int ArrayList::pop(int index)
{
    if (index < 0 || index >= _size)
        throw std::range_error("Index out of bounds for pop(int index).");

    int value = _data[index];
    remove(index);
    return value;
}

/**
* @brief Remove and return the last element of the list.
*
* @return The removed value.
* @throws std::range_error if the list is empty.
*/
int ArrayList::pop()
{
    if (_size == 0)
        throw std::range_error("pop() from empty ArrayList");

    int value = _data[_size - 1];
    _size--;
    // Automatically shrinking ArrayList object if it is less than 25% capacity in use
    if (_size < _capacity / 4)
        _shrink_to_fit();
    return value;
}

/**
* @brief Print the contents in a Python-like list format to std::cout.
*/
void ArrayList::print()
{
    std::cout << "ArrayList([";
    if (_size > 0)
    {
        for (int i = 0; i < _size; i++)
        {
            std::cout << _data[i];
            if (i + 1 < _size)
                std::cout << ", ";
        }
    }
    std::cout << "])\n";
}

/**
* @brief Random access operator with bounds checking.
*
* @param index Index of the element to access (0.._size-1).
* @return Reference to the element at @p index.
* @throws std::range_error if index is out of bounds.
*/
int &ArrayList::operator[](int index)
{
    if (index < 0 || index >= _size)
        throw std::range_error("Index is out of bounds");

    return _data[index];
}

/**
* @brief Return the index of the minimum element.
*
* @return Index of the smallest value.
* @throws std::range_error if the list is empty.
*/
int ArrayList::argmin()
{
    if (_size == 0)
        throw std::range_error("argmin on empty ArrayList object");

    int min_elem_index = 0;
    int min_elem_value = _data[0];
    for (int i = 1; i < _size; i++)
    {
        if (_data[i] < min_elem_value)
        {
            min_elem_value = _data[i];
            min_elem_index = i;
        }
    }

    return min_elem_index;
}

/**
* @brief Return the index of the maximum element.
*
* @return Index of the largest value.
* @throws std::range_error if the list is empty.
*/
int ArrayList::argmax()
{
    if (_size == 0)
        throw std::range_error("argmax on empty ArrayList object");

    int max_elem_index = 0;
    int max_elem_value = _data[0];
    for (int i = 1; i < _size; i++)
    {
        if (_data[i] > max_elem_value)
        {
            max_elem_value = _data[i];
            max_elem_index = i;
        }
    }

    return max_elem_index;
}

/**
* @brief Return the minimum element value.
*
* @return Smallest value in the list.
* @throws std::range_error if the list is empty.
*/
int ArrayList::min()
{
    if (_size == 0)
        throw std::range_error("min on empty ArrayList object");

    int min_value = _data[0];
    for (int i = 1; i < _size; i++)
        if (_data[i] < min_value)
            min_value = _data[i];

    return min_value;
}

/**
* @brief Return the maximum element value.
*
* @return Largest value in the list.
* @throws std::range_error if the list is empty.
*/
int ArrayList::max()
{
    if (_size == 0)
        throw std::range_error("max on empty ArrayList object");

    int max_value = _data[0];
    for (int i = 1; i < _size; i++)
        if (_data[i] > max_value)
            max_value = _data[i];

    return max_value;
}

/**
* @brief Count occurrences of a given value in the list.
*
* @param value The value to count.
* @return Number of occurrences of @p value.
*/
int ArrayList::count(int value)
{
    int counter = 0;
    for (int i = 0; i < _size; i++)
        if (_data[i] == value)
            counter++;

    return counter;
}
