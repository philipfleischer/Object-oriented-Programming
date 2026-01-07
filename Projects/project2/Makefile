# =========================
# Compiler setup
# =========================
CXX      = g++
CXXFLAGS = -std=c++14 -Wall -Wextra -O2 -Iinclude

# =========================
# Directories
# =========================
SRCDIR := src
INCDIR := include
OUTDIR := build
GENDIR := gen
DOCDIR := docs

# =========================
# Binaries & generated files
# =========================
BINS := $(OUTDIR)/array_list \
        $(OUTDIR)/linked_list \
        $(OUTDIR)/compare \
        $(OUTDIR)/lal

.PHONY: all clean run-compare plot run-all docs help

# =========================
# Default: build everything
# =========================
all: | $(OUTDIR) $(GENDIR) $(BINS)

# Ensure output dirs exist
$(OUTDIR):
	mkdir -p $(OUTDIR)

$(GENDIR):
	mkdir -p $(GENDIR)

# =========================
# Build rules
# (compile directly to binaries; simple project)
# =========================

# ArrayList tests
$(OUTDIR)/array_list: $(SRCDIR)/test_array_list.cpp $(SRCDIR)/array_list.cpp $(INCDIR)/array_list.h | $(OUTDIR)
	$(CXX) $(CXXFLAGS) $(SRCDIR)/test_array_list.cpp $(SRCDIR)/array_list.cpp -o $@

# LinkedList tests
$(OUTDIR)/linked_list: $(SRCDIR)/test_linked_list.cpp $(SRCDIR)/linked_list.cpp $(INCDIR)/linked_list.h | $(OUTDIR)
	$(CXX) $(CXXFLAGS) $(SRCDIR)/test_linked_list.cpp $(SRCDIR)/linked_list.cpp -o $@

# Timing / comparison program
# (links array_list.cpp and linked_list.cpp to provide definitions)
$(OUTDIR)/compare: $(SRCDIR)/compare_array_list_and_linked_list.cpp \
                   $(SRCDIR)/array_list.cpp $(SRCDIR)/linked_list.cpp \
                   $(INCDIR)/array_list.h $(INCDIR)/linked_list.h | $(OUTDIR)
	$(CXX) $(CXXFLAGS) $(SRCDIR)/compare_array_list_and_linked_list.cpp \
	                  $(SRCDIR)/array_list.cpp $(SRCDIR)/linked_list.cpp -o $@

# LinkedArrayList demo
$(OUTDIR)/lal: $(SRCDIR)/test_linked_array_list.cpp $(SRCDIR)/linked_array_list.cpp $(SRCDIR)/array_list.cpp \
               $(INCDIR)/linked_array_list.h $(INCDIR)/array_list.h | $(OUTDIR)
	$(CXX) $(CXXFLAGS) $(SRCDIR)/test_linked_array_list.cpp $(SRCDIR)/linked_array_list.cpp $(SRCDIR)/array_list.cpp -o $@

# =========================
# Run helpers
# =========================

# Run timing from gen/ so .txt end up in gen/
run-compare: $(OUTDIR)/compare
	@mkdir -p gen
	./$(OUTDIR)/compare

# Run plot from gen/ so it reads/writes inside gen/
plot: | $(GENDIR)
	@cd $(GENDIR) && python3 ../plot_timings.py

# Run everything (builds first)
run-all: all
	@echo "== Running array_list tests =="
	./$(OUTDIR)/array_list
	@echo "== Running linked_list tests =="
	./$(OUTDIR)/linked_list
	@echo "== Running comparison timing =="
	$(MAKE) run-compare
	@echo "== Plotting timings =="
	$(MAKE) plot
	@echo "== Running LinkedArrayList demo =="
	./$(OUTDIR)/lal

# =========================
# Docs
# =========================
docs:
	doxygen Doxyfile

# =========================
# Cleanup
# =========================
clean:
	@echo "Cleaning build and generated artifacts..."
	rm -rf $(OUTDIR)
	rm -rf $(GENDIR)/*.txt $(GENDIR)/*.png

help:
	@echo "Targets:"
	@echo "  all          - build all binaries"
	@echo "  run-all      - build & run tests, timing, plotting, and demo"
	@echo "  run-compare  - run timing binary (outputs .txt into gen/)"
	@echo "  plot         - run plot_timings.py from gen/"
	@echo "  docs         - generate doxygen docs"
	@echo "  clean        - remove build/ and generated files in gen/"
