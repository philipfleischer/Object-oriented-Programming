// array_list.cpp

#include <iostream>
#include <stdexcept>
#include "array_list.h"

/// @brief Resizes the internal array to a larger capacity.
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

    // Finding the smallest pwer of 2 to contain elements
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

/// @brief Default constructor for ArrayList: it initializes an empty ArrayList list object.
ArrayList::ArrayList()
{
    _capacity = 1;
    _size = 0;
    _data = new int[_capacity];
    _growth_factor = 2;
}

/// @brief Constructs ArrayList list with initial vector values.
ArrayList::ArrayList(const std::vector<int> &init)
{
    _growth_factor = 2;
    _size = static_cast<int>(init.size());
    _capacity = (_size == 0) ? 1 : _size;
    _data = new int[_capacity];
    for (int i = 0; i < _size; i++)
        _data[i] = init[static_cast<size_t>(i)];
}

/// @brief Destructor that frees the allocated memory.
ArrayList::~ArrayList()
{
    delete[] _data;
}

int ArrayList::length()
{
    return _size;
}

int ArrayList::capacity()
{
    return _capacity;
}

void ArrayList::append(int element)
{
    // Check if array _data need to be resized _resize
    if (_size == _capacity)
        _resize();

    _data[_size] = element;
    _size++;
}

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

int ArrayList::pop(int index)
{
    if (index < 0 || index >= _size)
        throw std::range_error("Index out of bounds for pop(int index).");

    int value = _data[index];
    remove(index);
    return value;
}

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

int &ArrayList::operator[](int index)
{
    if (index < 0 || index >= _size)
        throw std::range_error("Index is out of bounds");

    return _data[index];
}

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

int ArrayList::count(int value)
{
    int counter = 0;
    for (int i = 0; i < _size; i++)
        if (_data[i] == value)
            counter++;

    return counter;
}
