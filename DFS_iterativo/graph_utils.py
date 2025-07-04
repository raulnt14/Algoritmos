import networkx as nx

def build_digraph_with_weights():
    # num_nodes = 8
    # num_edges = 9
    # node1 = [1, 2, 2, 3, 3, 4, 4, 4, 5]
    # node2 = [4, 4, 5, 5, 8, 6, 7, 8, 7]
    # peso = [5, 2, 3, 1, 6, 8, 7, 6, 2]

    # num_nodes = 8
    # num_edges = 13
    #
    # node1 = [1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6, 7]
    # node2 = [2, 5, 3, 4, 5, 7, 8, 2, 6, 3, 4, 7, 8]
    # peso = [2, 5, 3, 4, 7, 8, 2, 6, 3, 4, 7, 8, 9]

    num_nodes = 9
    num_edges = 6

    node1 = [1,2,4,5,7,8]
    node2 = [2,3,5,6,8,9]
    peso = [2, 5, 3, 4, 7, 8]

    first_node = 1

    graph = nx.DiGraph()
    for i in range(1, num_nodes):
        graph.add_node(i)

    for i in range(num_edges):
        graph.add_edge(node1[i], node2[i], weight=peso[i])

    return(graph)