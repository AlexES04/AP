import minigraph as nx

def build_graph(edges_list, num_nodes, num_edges):

    graph = nx.Graph()

    for node in range(1, num_nodes + 1):
        graph.add_node(node)

    for edge in range(1, num_edges + 1):
        edges = edges_list[edge-1].split()
        graph.add_edge(int(edges[0]), int(edges[1]))

    return graph