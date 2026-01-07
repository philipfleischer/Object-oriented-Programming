#include <memory>
#include "array_list.h"

/// @brief  TODO: Doxygen documentation
struct ArrayListNode
{
    /// @brief  TODO: Doxygen documentation
    std::unique_ptr<ArrayList> val;

    /// @brief  TODO: Doxygen documentation
    ArrayListNode *prev;
    /// @brief  TODO: Doxygen documentation
    ArrayListNode *next;
    /// @brief  TODO: Doxygen documentation
    ArrayListNode(std::vector<int> values, ArrayListNode *prev, ArrayListNode *next);
};
