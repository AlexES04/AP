import os
import sys

actual_dir = os.path.dirname(os.path.abspath(__file__))
week04_dir = os.path.dirname(actual_dir)
sys.path.append(week04_dir)

import utils.minigraph as nx
from solve import solve_punto_reunion
from utils.utils import open_test_file, close_test_file, get_line

test_file = os.path.join(actual_dir, "test.txt")
input_source = open_test_file(test_file)

try:
    n, m, k = map(int, get_line(input_source).split())
    positions = list(map(int, get_line(input_source).split()))
    graph = nx.Graph()
    for u in range(1, n + 1):
        graph.add_node(u)
    for _ in range(m):
        u, v = map(int, get_line(input_source).split())
        graph.add_edge(u, v)
    point, radius = solve_punto_reunion(graph, positions)
    print(f'Punto={point}')
    print(f'DistanciaMaxima={radius}')
finally:
    close_test_file(test_file, input_source)