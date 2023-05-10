from visualization.graph_visualizer import draw_graph, highlight_path_on_graph, color_unused_nodes_grey, highlight_expanded_nodes
from visualization.labels import add_labels
import matplotlib.pyplot as plt


def reconstruct_path(cameFrom, current, start_node = 0):
    path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        path.append(current)
        if current == start_node:
            break
    return path[::-1]

def bfs(graph, start_node, goal_node):
    """Breadth-first search algorithm
    
    Arguments:
        graph {list} -- Graph represented as an adjacency list
        start_node {int} -- Start node
        goal_node {int} -- Goal node
    
    Returns:
        list -- Path from start node to goal node
    """
    frontier = [start_node]
    expanded = set()
    visited = set([start_node])
    cameFrom = {}
    
    while frontier:
        current_node = frontier.pop(0)
        expanded.add(current_node)
        
        if current_node == goal_node:
            return reconstruct_path(cameFrom, current_node, start_node), expanded, visited
        
        neighbors = graph[current_node]
        for neighbor in neighbors:
            if neighbor not in expanded and neighbor not in frontier:
                cameFrom[neighbor] = current_node
                frontier.append(neighbor)
                visited.add(neighbor)
    
    return None

def visualize_bfs(graph, start_node, goal_node, node_size=2000):
    """Visualize the BFS algorithm on a graph
    
    Arguments:
        graph {list} -- Graph represented as an adjacency list
        start_node {int} -- Start node
        goal_node {int} -- Goal node
        node_size {int} -- Size of each node in the graph visualization (default: {2000})"""

    node_numbers = [i for i in range(len(graph))]
    G, pos = draw_graph(graph, node_numbers, node_size=node_size)
    path, expanded, visited = bfs(graph, start_node, goal_node)
    G, pos = color_unused_nodes_grey(G, pos, visited, node_size=node_size)
    G, pos = highlight_expanded_nodes(G, pos, expanded, node_size=node_size)
    G, pos = highlight_path_on_graph(G, pos, path, node_size=node_size)
    plt.show()