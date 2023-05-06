from visualization.tree_visualizer import draw_tree
from visualization.graph_visualizer import highlight_path_on_graph, color_unused_nodes_grey
from visualization.labels import add_alpha_beta_values


def alpha_beta_search(tree_graph, leaf_values, node = 0, maximizing_player = True, alpha = -float("inf"), beta = float("inf")):
    """Returns the minimax value and the path to the node that achieves it.

    Args:
        tree_graph: A list of lists. The i-th element is a list of nodes that are connected to node i.
        values: A list of values. The i-th element is the value of node i.
        node: The node to start the minimax search from.
        maximizing_player: A boolean indicating whether the current player is the maximizing player.
        alpha: The alpha value.
        beta: The beta value.
    Returns:
        A tuple of (minimax_value, path, values_dict). The minimax value is the value of the node that achieves the minimax value.
        The path is a list of nodes that leads to the node that achieves the minimax value.
        The values_dict is a dictionary of tuples, where the tuple at key "i" represents the values for node "i".
    """
    leaf_values = [0] * (len(tree_graph) - len(leaf_values)) + leaf_values
    values_dict = {}
    minimax_value, chosen_path, values_dict = _alpha_beta_search(tree_graph, leaf_values, node, maximizing_player, alpha, beta, values_dict)
    return minimax_value, chosen_path[::-1], values_dict

def _alpha_beta_search(tree_graph, values, node, maximizing_player, alpha, beta, values_dict):
    if len(tree_graph[node]) == 0:
        return values[node], [node], {node: (values[node], alpha, beta)}
    
    chosen_path = None
    minimax_value = None
    for connected_node in tree_graph[node]:
        value, path, child_values_dict = _alpha_beta_search(tree_graph, values, connected_node, not maximizing_player, alpha, beta, values_dict)
        values_dict.update(child_values_dict)
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

    values_dict[node] = (minimax_value, alpha, beta)
    return minimax_value, chosen_path + [node], values_dict

def visualize_alpha_beta_search(tree_graph, leaf_values, node = 0, node_size = 2000):
    """Uses the tree_visualizer and graph_visualizer modules to visualize the alpha-beta search.
    It draws the tree and highlights the path that achieves the minimax value.
    It also shows the alpha and beta values.
    Nodes and edges that are not visited are colored gray.
    
    Args:
        tree_graph: A list of lists. The i-th element is a list of nodes that are connected to node i.
        values: A list of values. The i-th element is the value of node i.
        node: The node to start the alpha-beta search from.
    """
    minimax_value, chosen_path, values_dict = alpha_beta_search(tree_graph, leaf_values, node)
    G, pos = draw_tree(tree_graph, [], False, False, node_size)
    G, pos = highlight_path_on_graph(G, pos, chosen_path, node_size=node_size)
    G, pos = add_alpha_beta_values(G, pos, values_dict)
    G, pos = color_unused_nodes_grey(G, pos, values_dict, node_size=node_size)