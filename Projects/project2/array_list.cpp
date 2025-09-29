#include <iostream>
#include <stdexcept>
#include "array_list.h"

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

int& ArrayList::operator[](int index)
{
    if ((index < 0) || (index >= _size))
    {
        throw std::range_error("Index is out of bounds");
    }
    return _data[index];
}