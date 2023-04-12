import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(adj_list, labels):
    G = nx.Graph()

    for node, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=False, node_color='white', edgecolors='black', node_size=2000)

    for p, label in zip(pos.values(), labels):
        plt.text(p[0], p[1], label, ha='center', va='center', fontsize=12)

    plt.show()

# Example usage
adj_list = [[1, 2], [3, 4], [5, 6], [7, 8], [], [], [], [], []]

labels = [1.5, 6, 15, 4, 5, 6, 7, 8, 9]

draw_graph(adj_list, labels)