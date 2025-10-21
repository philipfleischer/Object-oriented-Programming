#include "linked_array_list.h"

ArrayListNode::ArrayListNode(std::vector<int> values,
                             ArrayListNode *prev,
                             ArrayListNode *next)
    : val(std::make_unique<ArrayList>(values)), prev(prev), next(next)
{
    // TODO: Need to implement for 4b here
}
