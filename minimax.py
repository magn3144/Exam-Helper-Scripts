import unittest


def minimax(tree_graph, values, node = 0):
    """Returns the minimax value and the path to the node that achieves it.

    Args:
        tree_graph: A list of lists. The i-th element is a list of nodes that are connected to node i.
        values: A list of values. The i-th element is the value of node i.
        node: The node to start the minimax search from.
    Returns:
        A tuple of (minimax_value, path). The minimax value is the value of the node that achieves the minimax value.
        The path is a list of nodes that leads to the node that achieves the minimax value.
    """
    values = [0] * (len(values) - 1) + values
    minimax_value, chosen_path = _minimax(tree_graph, values, node, True)
    return minimax_value, chosen_path[::-1]

def _minimax(tree_graph, values, node, maximizing_player):
    if len(tree_graph[node]) == 0:
        return values[node], [node]
    
    chosen_path = None
    minimax_value = None
    for connected_node in tree_graph[node]:
        value, path = _minimax(tree_graph, values, connected_node, not maximizing_player)
        if maximizing_player:
            if minimax_value == None or value > minimax_value:
                minimax_value = value
                chosen_path = path
        else:
            if minimax_value == None or value < minimax_value:
                minimax_value = value
                chosen_path = path

    return minimax_value, chosen_path + [node]