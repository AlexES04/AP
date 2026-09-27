import os
import sys

actual_dir = os.path.dirname(os.path.abspath(__file__))
week04_dir = os.path.dirname(actual_dir)
sys.path.append(week04_dir)

from utils.utils import *

test_file = os.path.join(actual_dir, "test.txt")
input_source = open_test_file (test_file)
    
# ----------------------------------------------------------------
import utils.minigraph as nx
from utils.graph_utils import *
from solve import *

first_line = get_line(input_source).split()
num_nodes  = int(first_line[0])
num_edges  = int(first_line[1])
edges_list = get_n_lines(input_source, num_edges)

graph = build_digraph_with_weights(edges_list, num_nodes, num_edges)

print("============ ITERATIVE ============")
iterative_solution = dfs_topological_sort_iterative(graph)
d_swap = {v: k for k, v in iterative_solution.items()}
print(dict(sorted(d_swap.items())))

print("============ RECURSIVE ============")
recursive_solution = dfs_topological_sort_recursive(graph)
d_swap = {v: k for k, v in recursive_solution.items()}
print(dict(sorted(d_swap.items())))


# --------------------------------------------------------------------
# Cerramos el fichero (si lo utilizamos para redireccionar la entrada)

close_test_file(test_file, input_source)