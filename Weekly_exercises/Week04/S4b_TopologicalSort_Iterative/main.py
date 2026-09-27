from utils import *

test_file    = "./Week04/S4b_TopologicalSort_Iterative/test.txt"
input_source = open_test_file (test_file)
    
# ----------------------------------------------------------------
import minigraph as nx
from graph_utils import *
from solve import *

first_line = get_line(input_source).split()
num_nodes  = int(first_line[0])
num_edges  = int(first_line[1])
edges_list = get_n_lines(input_source, num_edges)

graph = build_digraph_with_weights(edges_list, num_nodes, num_edges)

solution = dfs_topological_sort(graph)
d_swap = {v: k for k, v in solution.items()}

print(dict(sorted(d_swap.items())))

# --------------------------------------------------------------------
# Cerramos el fichero (si lo utilizamos para redireccionar la entrada)

close_test_file(test_file, input_source)