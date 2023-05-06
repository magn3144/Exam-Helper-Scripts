import networkx as nx
import matplotlib.pyplot as plt


def add_alpha_beta_values(G, pos, values_dict):
    # Create a dictionary with node labels containing minimax, alpha, and beta values
    node_labels = {node: f"{values_dict[node][0]}\n[{values_dict[node][1]}, {values_dict[node][2]}]" for node in G.nodes if node in values_dict.keys()}

    # Draw the node labels on the graph
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12, font_color='black')

    return G, pos

def add_astar_values(G, pos, node_numbers, h_values, g_values, f_values, edge_weights):
    """Add heuristic, g, and f values to the graph visualization
    Also add edge weights to the graph visualization
    
    Arguments:
        G {networkx.Graph} -- Graph to visualize
        pos {dict} -- Dictionary containing node positions
        h_values {dict} -- Dictionary containing heuristic values for each node
        g_values {dict} -- Dictionary containing g values for each node
        f_values {dict} -- Dictionary containing f values for each node
        edge_weights {dict} -- Dictionary containing edge weights for each edge"""

    # Create a dictionary with node labels containing heuristic, g, and f values
    node_labels = {node: f"{node_numbers[node]}\nh:{h_values[node]}\ng:{g_values[node]}\nf:{f_values[node]}" for node in G.nodes}

    # Draw the node labels on the graph
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12, font_color='black')

    # Create a dictionary with edge labels containing edge weights
    # G.edges contains two edges for each edge in the graph, so we need to filter out the duplicate edges
    edge_labels = {(u, v): edge_weights[(u, v)] for u, v in G.edges if (u, v) in edge_weights.keys()}

    # Draw the edge labels on the graph
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, font_color='black')

    return G, pos