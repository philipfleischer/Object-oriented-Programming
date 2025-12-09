# Project 2

## Commands

To compile the project:

- Write 'make all' in terminal to make all the files that shall be used in the project. This entails all the files for all the exercises.

To run the project:

- Write 'make run-all' in terminal to run all the main functions. This runs all the programs in the projects simultaneously.
- If you want to run the files one-by-one, simply write './path/chosen_file' in the terminal.
  - Note: The path may be /build/ if you want to run the output files generated. If you want to run the test-files, simply write './test_chosen_file' in terminal.

To clean the project:

- Write 'make clean' in the terminal. This removes all the output files generated in the /build/ directory.
- Note: It does not remove the genereated files like the .txt- and .png-file(s).

## List of exercises I managed to run and compile

We managed to run and compile all the files for all the parts. Furthermore, all the tests work without problem and looks correct. The generated files also look sound and align with expectations.

List:

- ArrayList (Part 1)
- LinkedList (Part 2)
- Timing and comparison (Part 3)
- LinkedArrayList (Part 4)

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

## Task 3b

### Estimated runtime expressions
   - ArrayList get: `T(N)` is approximately constant
   - ArrayList insert_front: `T(N)` is approximately `a*N + b`
   - LinkedList get: `T(N)` is approximately `a*N + b`
   - LinkedList insert_front: `T(N)` is approximately constant

## Task 3c

### Predictions and result

From task 3a we predicted that:

- Arraylist: get() -> O(1) and insert_front() -> O(n)
- LinkedList: get() -> O(n) and insert_front() -> O(1)

From task 3b we measured these results:

- ArrayList get()-function for average microseconds per access:

  - 100 -> 0.003
  - 1000 -> 0.003
  - 10000 -> 0.002
  - 100000 -> 0.002
  - These values represent a "flat" line on the graph, meaning it is in constant time complexity.

- ArrayList insert_front()-function for average microseconds per insert:

  - 100 -> 0.06
  - 1000 -> 0.117
  - 10000 -> 0.7773
  - 100000 -> 4.38338
  - These values represent a linear line on the graph, meaning it is in linear time complexity.

- LinkedList get()-function for average microseconds per access:

  - 100 -> 0.02
  - 1000 -> 0.171
  - 10000 -> 5.625
  - 100000 -> 53.903
  - These values represent a linear line on the graph, meaning it is in linear time complexity.

- LinkedList insert_front()-function for average microseconds per insert:
  - 100 -> 0.01
  - 1000 -> 0.0012
  - 10000 -> 0.0094
  - 100000 -> 0.0081
  - These values represent a "flat" line on the graph (Even decreasing as N grows), meaning it is in constant time complexity.

### Conclusion:

The predictions from task 3a corresponds with the results from task 3b.
There were some small surprises that was unexpected, but after reading some articles it seems the likely cause might be hardware, cache effects and pointer chasing, there was also decrease in the constant trend for insert-front, but that may be due to more efficient lookups and warmer components that increases the efficiency and reduces latency.
Overall the outputs to the txt files and the graphs from plot looks as expected and natural.

## Documentation Notes

- The documentations for the functions and classes were written extensively in the header files, and just short one-liners in the source files.
- The reason was to avoid duplication of documentation and unnecessarily long source files that become unorganized. I read that this was the way to do it in real life as well, in other words that this is the best documenation convention.

## Use of AI

- Some of the Doxygen documentation structure and README wording was generated and refined with OpenAI´s ChatGPT.
- All documentation and comments were revised and edited to accurately represent our projects files and structure.
- All source files, header files and test files were programmed by us. AI was only used for occasional debugging and explanation support.
