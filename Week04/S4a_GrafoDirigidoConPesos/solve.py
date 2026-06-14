import minigraph as nx

def build_digraph_with_weights(edges_list, num_nodes, num_edges):
    """ 
    Build the corresponding directed graph with weights. Nodes
    numbering starts with number 1 (that is, nodes are 1,2,3,...)
    """

    graph = nx.DiGraph()

    for node in range(1, num_nodes + 1):
        graph.add_node(node)

    for edge in range(num_edges):
        edges = edges_list[edge].split()
        graph.add_edge(int(edges[0]), int(edges[1]), int(edges[2]))

    return graph