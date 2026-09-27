import minigraph  as nx
from sys          import maxsize as infinite
from simple_stack import *


def dfs_recursive(graph, first_node):
    N = graph.number_of_nodes()
    
    visited = set()

    def dfs(node):
        visited.add(node)

        for neighbour in graph.neighbors(node):
            if neighbour not in visited:
                dfs(neighbour)

    dfs(first_node)

    return visited

def dfs_iterative(graph, first_node):
    N = graph.number_of_nodes()

    visited = set()
    stack = Stack()

    visited.add(first_node)
    stack.push(first_node)

    while not stack.isEmpty():
        current = stack.pop()
        for neighbour in graph.neighbors(current):
            if neighbour not in visited:
                visited.add(neighbour)
                stack.push(neighbour)
    return visited