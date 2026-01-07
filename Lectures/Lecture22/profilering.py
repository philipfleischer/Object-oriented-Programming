import cProfile
import numpy.random as npr
from line_profiler import LineProfiler
from drunk_walker import DrunkWalker, main

npr.seed(100122)  # Viktig for sammenligning
cProfile.run("DrunkWalker(100).walk_home()")

lp = LineProfiler()
# Først "pakke inn" funksjon som skal kalles i wrapper-objeckt
lp_wrapper = lp(main)
# Legge til andre funksjoner som kalles av main som vi også vil se på
lp.add_function(DrunkWalker.walk_home)
lp.add_function(DrunkWalker.step)
# Får wrapper-objektet til å kalle main(1), bruker samem argument (1)
lp_wrapper(1)
lp.print_stats()
