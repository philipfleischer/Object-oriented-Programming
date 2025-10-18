# --- Compiler setup ---
CXX      = g++
CXXFLAGS = -std=c++14 -Wall -Wextra -O2

# --- Default target ---
all: array_list
# Later: add 'linked_list' and 'compare_array_list_and_linked_list' here

# -------------------------------
# Build ArrayList (enabled now)
# -------------------------------
array_list: array_list.h array_list.cpp test_array_list.cpp
	$(CXX) $(CXXFLAGS) test_array_list.cpp array_list.cpp -o array_list

# -------------------------------
# Build LinkedList (enable later)
# -------------------------------
# linked_list: linked_list.h linked_list.cpp test_linked_list.cpp
# 	$(CXX) $(CXXFLAGS) test_linked_list.cpp linked_list.cpp -o linked_list

# -------------------------------
# Build comparison (enable later)
# -------------------------------
# compare_array_list_and_linked_list: compare_array_list_and_linked_list.cpp \
#                                     array_list.h array_list.cpp \
#                                     linked_list.h linked_list.cpp
# 	$(CXX) $(CXXFLAGS) compare_array_list_and_linked_list.cpp \
# 	array_list.cpp linked_list.cpp -o compare_array_list_and_linked_list

# -------------------------------
# Cleanup
# -------------------------------
clean:
	rm -f array_list linked_list compare_array_list_and_linked_list *.o
