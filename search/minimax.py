from visualization.tree_visualizer import draw_tree
from visualization.graph_visualizer import highlight_path_on_graph


def minimax(tree_graph, leaf_values, node = 0):
    """Returns the minimax value and the path to the node that achieves it.

    Args:
        tree_graph: A list of lists. The i-th element is a list of nodes that are connected to node i.
        values: A list of values. The i-th element is the value of node i.
        node: The node to start the minimax search from.
    Returns:
        A tuple of (minimax_value, path). The minimax value is the value of the node that achieves the minimax value.
        The path is a list of nodes that leads to the node that achieves the minimax value.
    """
    values = [0] * (len(tree_graph) - len(leaf_values)) + leaf_values
    _, chosen_path, combined_minimax_values = _minimax(tree_graph, values, node, True)
    combined_minimax_values_list = [combined_minimax_values[i] for i in range(len(combined_minimax_values))]
    return chosen_path[::-1], combined_minimax_values_list

def _minimax(tree_graph, values, node, maximizing_player):
    if len(tree_graph[node]) == 0:
        return values[node], [node], {node: values[node]}
    
    chosen_path = None
    minimax_value = None
    combined_minimax_values = {}
    for connected_node in tree_graph[node]:
        value, path, minimax_values = _minimax(tree_graph, values, connected_node, not maximizing_player)
        combined_minimax_values.update(minimax_values)
        if maximizing_player:
            if minimax_value == None or value > minimax_value:
                minimax_value = value
                chosen_path = path
        else:
            if minimax_value == None or value < minimax_value:
                minimax_value = value
                chosen_path = path
    combined_minimax_values[node] = minimax_value

    return minimax_value, chosen_path + [node], combined_minimax_values

def visualize_minimax(tree_graph, leaf_values, node = 0, node_size = 2000):
    """Uses the tree_visualizer and graph_visualizer modules to visualize the minimax search.
    
    Args:
        tree_graph: A list of lists. The i-th element is a list of nodes that are connected to node i.
        values: A list of values. The i-th element is the value of node i.
        node: The node to start the minimax search from.
    """
    chosen_path, minimax_values = minimax(tree_graph, leaf_values, node)
    G, pos = draw_tree(tree_graph, minimax_values)
    highlight_path_on_graph(G, pos, chosen_path, node_size)