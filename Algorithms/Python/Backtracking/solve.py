import minigraph  as nx
from simple_queue import *

def solve_backtracking(graph, first_node, target_node):
    all_solutions = []
    current_path = []
    visited = set()

    def backtrack(current_node):
        if current_node == target_node:
            current_path.append(current_node)
            all_solutions.append(list(current_path))
            current_path.pop()
            return

        visited.add(current_node)
        current_path.append(current_node)

        for neighbour in graph.neighbors(current_node):
            if neighbour not in visited:
                backtrack(neighbour)

        current_path.pop()
        visited.remove(current_node)

    backtrack(first_node)
    return all_solutions