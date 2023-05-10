from visualization.graph_visualizer import draw_graph, highlight_path_on_graph, color_unused_nodes_grey, highlight_expanded_nodes
from visualization.labels import add_labels
from search.breath_first_search import reconstruct_path
from tools.tools import add_costs_to_graph, seperate_graph_and_costs
import matplotlib.pyplot as plt


def best_first(graph, start_node, goal_node, h_values):
    cameFrom = {}
    expanded = set()
    visited = set([start_node])

    frontier = set([start_node])
    while frontier:
        current_node = min(frontier, key=lambda x: h_values[x])
        frontier.remove(current_node)
        expanded.add(current_node)

        if current_node == goal_node:
            return reconstruct_path(cameFrom, current_node, start_node), expanded, visited

        neighbors = graph[current_node]
        for neighbor in neighbors:
            frontier.add(neighbor)
            visited.add(neighbor)
            cameFrom[neighbor] = current_node

    return None

def visualize_best_first(graph, start_node, goal_node, heuristic_values, node_size=2000):
    """Visualize the A* algorithm on a graph
    
    Arguments:
        graph {list} -- Graph represented as an adjacency list
        start_node {int} -- Start node
        goal_node {int} -- Goal node
        heuristic_values {dict} -- Dictionary containing heuristic values for each node
        cost {int} -- Cost of each edge if all edges have the same cost (default: {None})
        node_size {int} -- Size of each node in the graph visualization (default: {2000})"""

    G, pos = draw_graph(graph, [], node_size=node_size)
    path, expanded, visited = best_first(graph, start_node, goal_node, heuristic_values)
    G, pos = color_unused_nodes_grey(G, pos, visited, node_size=node_size)
    G, pos = highlight_expanded_nodes(G, pos, expanded, node_size=node_size)
    G, pos = highlight_path_on_graph(G, pos, path, node_size=node_size)
    node_numbers = [i for i in range(len(graph))]
    label_values = zip(node_numbers, heuristic_values)
    G, pos = add_labels(G, pos, ("", "h"), label_values, {})
    plt.show()