from visualization.graph_visualizer import draw_graph, highlight_path_on_graph
from visualization.labels import add_astar_values


def reconstruct_path(cameFrom, current):
    path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        path.append(current)
    return path[::-1]

def A_star(graph, start_node, goal_node, heuristic_values, cost = None):
    g_values = [float("inf")] * len(heuristic_values)
    f_values = [float("inf")] * len(heuristic_values)
    g_values[start_node] = 0
    f_values[start_node] = heuristic_values[start_node]
    cameFrom = {}

    if cost != None:
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                graph[i][j] = (graph[i][j], cost)

    frontier = set([start_node])
    while frontier:
        current_node = min(frontier, key=lambda x: f_values[x])
        frontier.remove(current_node)

        if current_node == goal_node:
            return reconstruct_path(cameFrom, current_node), g_values, f_values

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

    labels = [i for i in range(len(graph))]
    G, pos = draw_graph(graph, [])
    path, g_values, f_values = A_star(graph, start_node, goal_node, heuristic_values, cost)
    G, pos = highlight_path_on_graph(G, pos, path, node_size=node_size)
    # Dictionary containing edge weights for each edge
    edge_weights = {}
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            edge_weights[(i, graph[i][j][0])] = graph[i][j][1]
    G, pos = add_astar_values(G, pos, labels, heuristic_values, g_values, f_values, edge_weights)