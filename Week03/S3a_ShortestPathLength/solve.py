import minigraph  as nx
from sys          import maxsize as infinite
from simple_queue import *

def bfs_path_length(graph, first_node):
    """
    Compute the shortest path length of the non-directed graph G
    starting from node first_node. Return a dictionary with the
    distance (in number of steps) from first_node to all the nodes.
    """

    distance = {}    
    visited = {first_node}
    nodes = Queue()

    for node in graph.nodes():
        distance[node] = infinite

    distance[first_node] = 0
    nodes.enqueue(first_node)
    
    while not nodes.isEmpty():
        current = nodes.dequeue()

        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[current] + 1
                nodes.enqueue(neighbor)


    return distance