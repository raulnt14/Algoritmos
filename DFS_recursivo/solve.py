import networkx as nx


def dfs_topological_sort(graph):
    """
    Compute one topological sort of the given graph.
    """

    # La solucion que retorna esta función es un diccionario de Python.
    #   * La clave del diccionario es el número del nodo
    #   * El valor es el orden topologico asignado a ese nodo
    #
    # Por ejemplo, si tenemos el siguiente grafo dirigido con 3 vertices:
    #                    3 ---> 2 ---> 1
    # ... el orden topologico es:
    #                El vértice 3 va en la primera posición
    #                El vértice 2 en la segunda posición
    #                El vértice 1 en la tercera posición
    # Con lo que debemos devolver un diccionario con este contenido:
    #     {1: 3, 2: 2, 3: 1}

    N = graph.number_of_nodes()

    visibleNodes = set()  # En este ejercicio utilizamos un set
    # para recordar los nodos visibles
    order = {}

    # solve it here! ------------------------------------------------

    def dfs(u):
        nonlocal N
        # 1. Añade código aqui
        # ...
        visibleNodes.add(u)
        for new_node in graph.neighbors(u):
            if (new_node not in visibleNodes):
                dfs(new_node)
        order[u] = N
        N = N - 1
        return

    # 2. Añade código también aqui
    # ...
    for nodo in (graph.nodes()):
        if(nodo not in visibleNodes):
            dfs(nodo)


    return order
