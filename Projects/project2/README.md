# H25_project2_philipef_stanisok_susanhop

Project 2 for philipef (philipef@mail.uio.no) and stanisok (stanisok@mail.uio.no) and susanhop (susanhop@mail.uio.no)

## Task 3a

### Algorithm analyses for ArrayList and LinkedList

When analyzing algorithms, it is beneficial to have a way to describe the cost of the operations it needs in terms of time complexity for the algorithm. We use Big-O notation to abstract over the results.

- Big O notation gives us an upper-bound regarding the time complexity´s increment in accordance with the increase of input n. An example is that O(1), which is constant time complexity will be constant regardless of the input. O(n), linear time complexity constitutes a linear growth in accordance to the input n.
- Amortized complexity is used when the worst case happens occasionally and the average running time is lower. By doing this we can get a clear grasp of the difference in theory and the algorithms used in the real world.
  It is important to have this kind of algorithm analysis with big-O and amortized complexity, since we can learn which operations and datastructures to use in different contexts.

### Functions analyzed

1. Get element at index i

   - ArrayList: Time complexity of O(1), constant time. The reason is that the elements are directly next to each other in memory, therefore we can access the elements using pointers, thereby jumping straight to the element instead of traversing the list.
   - LinkedList: Time complexity of O(n), linear time. The reason is that why dont store elements contiguosly in memory, but rather having pointers from the nodes to the next nodes. This means that in the worst case, we need to traverse the whole list to find an element. We can minimize the cost in a doubly linked list by choosing either head or tail, but it will still grow in linear time.

2. Insert at front

   - ArrayList: Time complexity of O(n), linear time. The reason is that when we insert an element at the front of the arraylist, we need to shift the position of all the other nodes.
   - LinkedList: Time complexity of O(1), constant time. The rason is that the header pointer can be replaced by the new element, and the original header can set it previous pointer to point at the new header. This means no other ondes need to be shifted.

3. Insert at back (append)

   - ArrayList: Time complexity of O(n), linear time in the worst case, but O(1) amortized time complexity for average cases. The reason is that for the constant time complexity method, we just select the tail node to be the new element and assign prev and next pointers to it. This is the average case, but we can also have the case where the ArrayList object is full and when we try to append, we end up having to resize the array. Resizing takes O(n) time, so O(1) time for the append plus O(n) time for the copy into a new array equals a total time complexity of O(n) in the worst case.
   - LinkedList: Time complexity of O(1), constant time. The reason is that we can just update the tail pointer for the newly allocated node and do the pointer updates.

4. Insert in the middle (at index i)

   - ArrayList: Time complexity of O(n), linear time. The reason is the same as for insertion at the front, since we need to shift all elements occuring after one position.
   - LinkedList: Time complexity of O(n), linear time. The same reason as insertion at front, since we need to traverse from head or tail node until we reach node at index i and then do a insertion that takes O(1) time (neighbour relinking only here). The cost can be reduced by selecting a smarter start pointer here as well.

5. Remove from front

   - ArrayList: Time complexity of O(n), linear time. The reason is that we need to shift the position of all elements occurring later one position to the left.
   - LinkedList: Time complexity of O(1), constant time. The reason is that we can just change the header pointer to the new element and update the next node to point to the new node and vice versa.

6. Remove from back

   - ArrayList: Time complexity of O(n), linear time complexity in the worst case. O(1), amortized constant time complexity on average. The reason is that normally we will just decrement the size counter for the array, but if we end up under 25% capacity usage, the \_shrink_to_fit() function gets called, which copies all elements over in a smaller array, which takes O(n) time.
   - LinkedList: Time complexity of O(1), constant time. The reason it is constant time is just that we can update the tail pointer to be tail->prev.

7. Remove from middle (at index i)

   - ArrayList: Time complexity of O(n), linear time complexity. The reason is that we need to shift all elements one position from the middle to the right.
   - LinkedList: Time complexity of O(n), linear time complexity. The reason is that we need to traverse the list to the index to remove it.

8. Print the list

   - ArrayList: Time complexity of O(n), linear time complexity. The reason is simply that we need to visit every node in the array and print it.
   - LinkedList: Time complexity of O(n), linear time complexity. The reason is that we need to visit every node in the linked list and print it.

### Conclusion:

- ArrayList has contiguos memory placement, which gives it constant time lookup and appending, however operations on other parts of the array as front and middle require shifting of the other elements which results in linear time complexity.
- LinkedList excels at insertions and deletions at the ends in constant time, it is also efficient at middle access operations since it does not need to shift indexes. Traversal cost is linear.
  So choosing between the two datastructures is up to the developers´ goals, where ArrayList is beneficial for many lookups and appends, while LinkedList is beneficial for insertions and removals from various parts of the list.
