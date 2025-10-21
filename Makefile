# --- Compiler setup ---
CXX      = g++
CXXFLAGS = -std=c++14 -Wall -Wextra -O2

# --- Output directories and files ---
OUTDIR := build
BINS   := $(OUTDIR)/array_list $(OUTDIR)/linked_list $(OUTDIR)/compare $(OUTDIR)/lal
GEN    := $(OUTDIR)/*.o $(OUTDIR)/*.txt $(OUTDIR)/arraylist_vs_linkedlist.png

.PHONY: all clean run-compare plot run-all

# --- Default target: build everything ---
all: $(OUTDIR) $(BINS)

# Ensure build directory exists before compiling
$(OUTDIR):
	mkdir -p $(OUTDIR)

# -------------------------------
# Build ArrayList (tests)
# -------------------------------
$(OUTDIR)/array_list: array_list.h array_list.cpp test_array_list.cpp | $(OUTDIR)
	$(CXX) $(CXXFLAGS) test_array_list.cpp array_list.cpp -o $@

# -------------------------------
# Build LinkedList (tests)
# -------------------------------
$(OUTDIR)/linked_list: linked_list.h linked_list.cpp test_linked_list.cpp | $(OUTDIR)
	$(CXX) $(CXXFLAGS) test_linked_list.cpp linked_list.cpp -o $@

# -------------------------------
# Timing / comparison program
# -------------------------------
$(OUTDIR)/compare: compare_array_list_and_linked_list.cpp array_list.cpp linked_list.cpp array_list.h linked_list.h | $(OUTDIR)
	$(CXX) $(CXXFLAGS) compare_array_list_and_linked_list.cpp array_list.cpp linked_list.cpp -o $@

# -------------------------------
# Linked Array List demo
# -------------------------------
$(OUTDIR)/lal: linked_array_list.cpp linked_array_list.h array_list.cpp array_list.h test_linked_array_list.cpp | $(OUTDIR)
	$(CXX) $(CXXFLAGS) test_linked_array_list.cpp linked_array_list.cpp array_list.cpp -o $@

# -------------------------------
# Run helpers
# -------------------------------
run-compare: $(OUTDIR)/compare
	./$(OUTDIR)/compare

plot:
	python3 plot_timings.py

# Run everything (builds first)
run-all: all
	@echo "== Running array_list tests =="
	./$(OUTDIR)/array_list
	@echo "== Running linked_list tests =="
	./$(OUTDIR)/linked_list
	@echo "== Running comparison timing =="
	./$(OUTDIR)/compare
	@echo "== Plotting timings =="
	$(MAKE) plot
	@echo "== Running LinkedArrayList demo =="
	./$(OUTDIR)/lal

# -------------------------------
# Cleanup
# -------------------------------
clean:
	rm -rf $(OUTDIR)
