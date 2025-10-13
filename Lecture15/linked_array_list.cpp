#include "linked_array_list.h"
#include "array_list.h"

// En struct kan også ha en konstruktør, og i dette tilfellet trenger vi en
ArrayListNode::ArrayListNode(std::vector<int> values, ArrayListNode *prevnode, ArrayListNode *nextnode)
{
    // En smart peker: minnet ryddes automatisk opp, trenger ikke delete eller free av minne. Kaller konstruktøren til ArrayList med values som argument
    val = std::make_unique<ArrayList>(values);

    prev = prevnode;
    next = nextnode;
}

// Kun for livekoding i forelesning - ikke prosjekt 2
int main()
{
    std::vector<int> v = std::vector<int>({1, 2, 3});
    ArrayListNode aln = ArrayListNode(v, nullptr, nullptr);
    std::cout << "Suksess!" << std::endl;
}
