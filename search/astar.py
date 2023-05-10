from visualization.graph_visualizer import draw_graph, highlight_path_on_graph, color_unused_nodes_grey
from visualization.labels import add_astar_values
from search.breath_first_search import reconstruct_path
from tools.tools import add_costs_to_graph
import matplotlib.pyplot as plt


def A_star(graph, start_node, goal_node, heuristic_values):
    g_values = [float("inf")] * len(heuristic_values)
    f_values = [float("inf")] * len(heuristic_values)
    g_values[start_node] = 0
    f_values[start_node] = heuristic_values[start_node]
    cameFrom = {}

    frontier = set([start_node])
    while frontier:
        current_node = min(frontier, key=lambda x: f_values[x])
        frontier.remove(current_node)

        if current_node == goal_node:
            return reconstruct_path(cameFrom, current_node, start_node), g_values, f_values

        neighbors = graph[current_node]
        for neighbor in neighbors:
            g_current = g_values[current_node]
            g_neighbor = g_current + neighbor[1]
            f_neighbor = g_neighbor + heuristic_values[neighbor[0]]
            
            if g_neighbor < g_values[neighbor[0]]:
                g_values[neighbor[0]] = g_neighbor
                f_values[neighbor[0]] = f_neighbor
                cameFrom[neighbor[0]] = current_node
                frontier.add(neighbor[0])

    return None

def visualize_astar(graph, start_node, goal_node, heuristic_values, cost = None, node_size=2000):
    """Visualize the A* algorithm on a graph
    
    Arguments:
        graph {list} -- Graph represented as an adjacency list
        start_node {int} -- Start node
        goal_node {int} -- Goal node
        heuristic_values {dict} -- Dictionary containing heuristic values for each node
        cost {int} -- Cost of each edge if all edges have the same cost (default: {None})
        node_size {int} -- Size of each node in the graph visualization (default: {2000})"""

    if cost != None:
        graph_with_costs = add_costs_to_graph(graph, cost)

    labels = [i for i in range(len(graph_with_costs))]
    G, pos = draw_graph(graph, [], node_size=node_size)
    path, g_values, f_values = A_star(graph_with_costs, start_node, goal_node, heuristic_values)
    G, pos = highlight_path_on_graph(G, pos, path, node_size=node_size)
    # Dictionary containing edge weights for each edge
    edge_weights = {}
    for i in range(len(graph_with_costs)):
        for j in range(len(graph_with_costs[i])):
            edge_weights[(i, graph_with_costs[i][j][0])] = graph_with_costs[i][j][1]
    G, pos = add_astar_values(G, pos, labels, heuristic_values, g_values, f_values, edge_weights)
    visited_nodes = [node for node, f_value in enumerate(f_values) if f_value != float("inf")]
    color_unused_nodes_grey(G, pos, visited_nodes, node_size=node_size)
    plt.show()