def alpha_beta_search(tree_graph, values, node, maximizing_player = True, alpha = -float("inf"), beta = float("inf")):
    if len(tree_graph[node]) == 0:
        return values[node], [node]
    
    chosen_path = None
    minimax_value = None
    for connected_node in tree_graph[node]:
        value, path = alpha_beta_search(tree_graph, values, connected_node, not maximizing_player)
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