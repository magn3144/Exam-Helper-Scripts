import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(adj_list, labels, node_size = 2000):
    G = nx.Graph()

    for node, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=False, node_color='white', edgecolors='black', node_size=node_size)

    if len(labels) > 0:
        for i, p in pos.items():
            plt.text(p[0], p[1], labels[i], ha='center', va='center', fontsize=12)
    
    return G, pos

def highlight_path_on_graph(G, pos, path, node_size=2000):
    # Draw the path edges with a different color and width
    path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    # Draw the path nodes with a different border color and width
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='white', edgecolors='red', node_size=node_size, linewidths=2)

    return G, pos

def color_unused_nodes_grey(G, pos, visited_nodes, node_size=2000):
    # Find the nodes that are not visited
    unused_nodes = [node for node in G.nodes if node not in visited_nodes]

    # Draw the unused nodes with grey border and white fill
    nx.draw_networkx_nodes(G, pos, nodelist=unused_nodes, node_color='white', edgecolors='grey', node_size=node_size, linewidths=2)

    # Find the edges between unused nodes and edges between used and unused nodes
    unused_edges = [(u, v) for u, v in G.edges if (u not in visited_nodes) or (v not in visited_nodes)]

    # Draw the unused edges with grey color and width
    nx.draw_networkx_edges(G, pos, edgelist=unused_edges, edge_color='grey', width=2)

    return G, pos

def highlight_expanded_nodes(G, pos, expanded_nodes, node_size=2000):
    # Draw the expanded nodes with a different width
    nx.draw_networkx_nodes(G, pos, nodelist=expanded_nodes, node_color='white', edgecolors='black', node_size=node_size, linewidths=2)

    # Draw the edges between expanded nodes with a different width
    expanded_edges = [(u, v) for u, v in G.edges if (u in expanded_nodes) and (v in expanded_nodes)]
    nx.draw_networkx_edges(G, pos, edgelist=expanded_edges, edge_color='black', width=2)

    return G, pos