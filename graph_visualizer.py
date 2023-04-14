import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(adj_list, labels, show_plot = False):
    G = nx.Graph()

    for node, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=False, node_color='white', edgecolors='black', node_size=2000)

    for p, label in zip(pos.values(), labels):
        plt.text(p[0], p[1], label, ha='center', va='center', fontsize=12)

    if show_plot:
        plt.show()
    
    return G, pos

def draw_graph_with_highlighted_path(G, pos, path, show_plot=False):
    # Draw the path edges with a different color and width
    path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    # Draw the path nodes with a different border color and width
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='white', edgecolors='red', node_size=2000, linewidths=2)

    if show_plot:
        plt.show()

    return G, pos

adj_list = [
    [1, 2],
    [0, 3],
    [0, 3],
    [1, 2, 4],
    [3]
]

labels = ['A', 'B', 'C', 'D', 'E']
path = [0, 1, 3, 4]

G, pos = draw_graph(adj_list, labels)
G, pos = draw_graph_with_highlighted_path(G, pos, path, show_plot=True)