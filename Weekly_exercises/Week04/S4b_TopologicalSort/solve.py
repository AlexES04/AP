import os
import sys

actual_dir = os.path.dirname(os.path.abspath(__file__))
week04_dir = os.path.dirname(actual_dir)
sys.path.append(week04_dir)

from utils.simple_stack import *

test_file = os.path.join(actual_dir, "test.txt")

def dfs_topological_sort_recursive(graph):
    N = graph.number_of_nodes()
    
    visibleNodes = set()  
    order = {}

    def dfs(u):
        nonlocal N
        visibleNodes.add(u)

        for neighbour in graph.neighbors(u):
            if neighbour not in visibleNodes:
                dfs(neighbour)
        
        order[u] = N
        N -= 1
        return

    for node in graph.nodes():
        if node not in visibleNodes:
            dfs(node)
    return order

def dfs_topological_sort_iterative(graph):
    N = graph.number_of_nodes()
    
    visibleNodes = set()  
    order = {}
    stack = Stack()

    for node in graph.nodes():
        if node not in visibleNodes:
            stack.push((node, False))

            while not stack.isEmpty():
                current, finished = stack.pop()
                if finished:
                    order[current] = N
                    N -= 1
                else:
                    if current in visibleNodes:
                        continue

                    visibleNodes.add(current)
                    stack.push((current, True))

                    for neighbour in graph.neighbors(current):
                        if neighbour not in visibleNodes:
                            stack.push((neighbour, False))
    return order
