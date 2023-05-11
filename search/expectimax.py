from visualization.tree_visualizer import draw_tree
from visualization.graph_visualizer import highlight_path_on_graph
import matplotlib.pyplot as plt


def expectimax(tree_graph, leaf_values, node = 0):
    """Returns the expectimax value and the path to the node that achieves it.

    Args:
        tree_graph: A list of lists. The i-th element is a list of nodes that are connected to node i.
        values: A list of values. The i-th element is the value of node i.
        node: The node to start the expectimax search from.
    Returns:
        A tuple of (expectimax_value, path). The expectimax value is the value of the node that achieves the expectimax value.
        The path is a list of nodes that leads to the node that achieves the expectimax value.
    """

    values = [0] * (len(tree_graph) - len(leaf_values)) + leaf_values
    _, combined_expectimax_values = _expectimax(tree_graph, values, node, True)
    combined_expectimax_values_list = [combined_expectimax_values[i] for i in range(len(combined_expectimax_values))]
    return combined_expectimax_values_list

def _expectimax(tree_graph, values, node, maximizing_player):
    if len(tree_graph[node]) == 0:
        return values[node], {node: values[node]}
    
    last_expectimax_values = []
    combined_expectimax_values = {}
    for connected_node in tree_graph[node]:
        value, expectimax_values = _expectimax(tree_graph, values, connected_node, not maximizing_player)
        combined_expectimax_values.update(expectimax_values)
        last_expectimax_values.append(value)
    if maximizing_player:
        expectimax_value = max(last_expectimax_values)
    else:
        expectimax_value = sum(last_expectimax_values) / len(last_expectimax_values)
    combined_expectimax_values[node] = expectimax_value

    return expectimax_value, combined_expectimax_values

def visualize_expectimax(tree_graph, leaf_values, node = 0, node_size = 2000):
    """Uses the tree_visualizer and graph_visualizer modules to visualize the expectimax search.
    
    Args:
        tree_graph: A list of lists. The i-th element is a list of nodes that are connected to node i.
        values: A list of values. The i-th element is the value of node i.
        node: The node to start the expectimax search from.
    """

    expectimax_values = expectimax(tree_graph, leaf_values, node)
    G, pos = draw_tree(tree_graph, expectimax_values)
    plt.show()