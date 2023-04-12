import networkx as nx
import matplotlib.pyplot as plt

def draw_tree(adj_list, labels, node_size = 2000):
    G = nx.Graph()

    for node, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.drawing.nx_agraph.graphviz_layout(G, prog='dot')
    nx.draw(G, pos, with_labels=False, node_color='white', edgecolors='black', node_size=node_size)

    for p, label in zip(pos.values(), labels):
        plt.text(p[0], p[1], label, ha='center', va='center', fontsize=12)

    plt.show()

# Example usage
adj_list = [[1, 2, 4], [3], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20], [21, 22], [23, 24], [], [], [], [], [], [], [], [], [], [], [], [], []]

labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
side_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']

draw_tree(adj_list, labels)