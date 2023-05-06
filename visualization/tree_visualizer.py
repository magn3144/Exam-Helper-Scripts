import networkx as nx
import matplotlib.pyplot as plt

def draw_tree(adj_list, labels = [], show_plot = False, node_numbers = False, node_size = 2000):
    G = nx.Graph()

    for node, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.drawing.nx_agraph.graphviz_layout(G, prog='dot')
    nx.draw(G, pos, with_labels=node_numbers, node_color='white', edgecolors='black', node_size=node_size)

    for p, label in zip(pos.values(), labels):
        plt.text(p[0], p[1], label, ha='center', va='center', fontsize=12)

    if show_plot:
        plt.show()
    
    return G, pos