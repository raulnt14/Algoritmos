import networkx as nx
from sys import maxsize as infinite
from simple_queue import *

num_nodes = 9
num_edges = 11
node1 = [1,2,3,4,5,6,7,8,8,9,9]
node2 = [4,8,6,7,2,9,1,5,6,7,3]
first_node = 1

# Paso 1: Crear un grafo unidirecional con num_nodes
graph = nx.Graph()
for i in range(1, num_nodes):
    graph.add_node(i)

# Paso 2: Añadirle las aristas
for i in range(num_edges):
    graph.add_edge(node1[i], node2[i])

#nx.draw(graph, with_labels=True, font_weight='bold')
#plt.show()

distance = {}
cola = Queue()
visibles = []

for node in graph.nodes():
    distance[node] = infinite

distance[0] = 0
cola.enqueue(first_node)
while len(visibles)<len(distance):



print(visibles)