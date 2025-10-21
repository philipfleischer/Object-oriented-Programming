# --- Compiler setup ---
CXX      = g++
CXXFLAGS = -std=c++14 -Wall -Wextra -O2

.PHONY: all clean run-compare plot

# --- Default target ---
all: array_list linked_list compare

# -------------------------------
# Build ArrayList (tests)
# -------------------------------
array_list: array_list.h array_list.cpp test_array_list.cpp
	$(CXX) $(CXXFLAGS) test_array_list.cpp array_list.cpp -o array_list

# -------------------------------
# Build LinkedList (tests)
# -------------------------------
linked_list: linked_list.h linked_list.cpp test_linked_list.cpp
	$(CXX) $(CXXFLAGS) test_linked_list.cpp linked_list.cpp -o linked_list

# -------------------------------
# Timing / comparison program
# (compare_array_list_and_linked_list.cpp must include only headers)
# -------------------------------
compare: compare_array_list_and_linked_list.cpp array_list.cpp linked_list.cpp array_list.h linked_list.h
	$(CXX) $(CXXFLAGS) compare_array_list_and_linked_list.cpp array_list.cpp linked_list.cpp -o compare

run-compare: compare
	./compare

plot:
	python3 plot_timings.py

# -------------------------------
# Cleanup
# -------------------------------
clean:
	rm -f array_list linked_list compare *.o *.txt arraylist_vs_linkedlist.png
