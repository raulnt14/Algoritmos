import networkx as nx
import matplotlib.pyplot as plt
from graph_utils import *
from solve import *

graph = build_digraph_with_weights()
nx.draw(graph, with_labels=True, font_weight='bold')
plt.show()

assert nx.is_directed_acyclic_graph(graph)

solution = dfs_topological_sort(graph)
d_swap = {v: k for k, v in solution.items()}

print(dict(sorted(d_swap.items())))