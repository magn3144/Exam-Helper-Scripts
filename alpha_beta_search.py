def alpha_beta_search(tree_graph, values, node = 0, maximizing_player = True, alpha = -float("inf"), beta = float("inf")):
    """Returns the minimax value and the path to the node that achieves it.

    Args:
        tree_graph: A list of lists. The i-th element is a list of nodes that are connected to node i.
        values: A list of values. The i-th element is the value of node i.
        node: The node to start the minimax search from.
        maximizing_player: A boolean indicating whether the current player is the maximizing player.
        alpha: The alpha value.
        beta: The beta value.
    Returns:
        A tuple of (minimax_value, path). The minimax value is the value of the node that achieves the minimax value.
        The path is a list of nodes that leads to the node that achieves the minimax value.
    """
    values = [0] * (len(values) - 1) + values
    minimax_value, chosen_path = _alpha_beta_search(tree_graph, values, node, maximizing_player, alpha, beta)
    return minimax_value, chosen_path[::-1]

def _alpha_beta_search(tree_graph, values, node, maximizing_player, alpha, beta):
    if len(tree_graph[node]) == 0:
        return values[node], [node]
    
    chosen_path = None
    minimax_value = None
    for connected_node in tree_graph[node]:
        value, path = _alpha_beta_search(tree_graph, values, connected_node, not maximizing_player, alpha, beta)
        if maximizing_player:
            if minimax_value == None or value > minimax_value:
                minimax_value = value
                chosen_path = path
            alpha = max(alpha, minimax_value)
        else:
            if minimax_value == None or value < minimax_value:
                minimax_value = value
                chosen_path = path
            beta = min(beta, minimax_value)
        if beta <= alpha:
                break

    return minimax_value, chosen_path + [node]