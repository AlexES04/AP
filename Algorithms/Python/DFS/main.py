from utils import *

test_file    = "./Algorithms/Python/utils/test.txt"
input_source = open_test_file(test_file)

# ----------------------------------------------------------------
import minigraph as nx
from graph_utils import *
from solve import *

first_line = input_source.readline().split()
num_nodes  = int(first_line[0])
num_edges  = int(first_line[1])
edges_list = get_n_lines(input_source, num_edges)

# Añade al fichero graph_utils.py tu función para crear un
# grafo no dirigido sin pesos
graph = build_graph(edges_list, num_nodes, num_edges);

first_node = 1
recursive_algorithm = dfs_recursive(graph, first_node)
iterative_algorithm = dfs_iterative(graph, first_node)

print("==================== RECURSIVE ====================")
print(recursive_algorithm)
print("==================== ITERATIVE ====================")
print (iterative_algorithm)

# --------------------------------------------------------------------
# Cerramos el fichero (si lo utilizamos para redireccionar la entrada)

close_test_file(test_file, input_source)