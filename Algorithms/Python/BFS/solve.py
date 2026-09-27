import minigraph  as nx
from sys          import maxsize as infinite
from simple_queue import *

def bfs_algorithm(graph, first_node):

    visited = set()
    queue = Queue()
    visited.add(first_node)
    queue.enqueue(first_node)

    while not queue.isEmpty():
        current = queue.dequeue()
        for neighbour in graph.neighbors(current):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.enqueue(neighbour)
            
    return visited