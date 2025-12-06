#include "array_list.h"

void ArrayList::_resize()
{
    _capacity *= _growth_factor;

    // New array (pointer)
    int *new_data = new int[_capacity];

    // Copy data old --> new array
    for (int i = 0; i < _size; i++)
    {
        new_data[i] = _data[i];
    }

    // Deleting old array - cleaning up after new
    delete _data;

    // Using new array hereafter
    _data = new_data;
}

ArrayList::ArrayList()
{
    _capacity = 1;
    _size = 0;
    _data = new int[_capacity];
    _growth_factor = 2;
}

ArrayList::~ArrayList()
{
    delete[] _data;
}

int ArrayList::length()
{
    return _size;
}

void ArrayList::append(int element)
{
    // Check if array _data need to be resized _resize
    if (_size == _capacity)
    {
        _resize();
    }
    _data[_size] = element;
    _size++;
}

int ArrayList::get(int index)
{
    if ((index < 0) || (index >= _size))
    {
        throw std::range_error("Index is out of bounds");
    }
    return _data[index];
}

void ArrayList::print()
{
    std::cout << "ArrayList([";
    for (int i = 0; i < _size - 1; i++)
    {
        std::cout << _data[i] << ", ";
    }
    std::cout << _data[_size - 1] << "])" << std::endl;
}

int &ArrayList::operator[](int index)
{
    if ((index < 0) || (index >= _size))
    {
        throw std::range_error("Index is out of bounds");
    }
    return _data[index];
}
