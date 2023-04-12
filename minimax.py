import unittest


def minimax(tree_graph, values, node, maximizing_player = True):
    if len(tree_graph[node]) == 0:
        return values[node], [node]
    
    chosen_path = None
    minimax_value = None
    for connected_node in tree_graph[node]:
        value, path = minimax(tree_graph, values, connected_node, not maximizing_player)
        if maximizing_player:
            if minimax_value == None or value > minimax_value:
                minimax_value = value
                chosen_path = path
        else:
            if minimax_value == None or value < minimax_value:
                minimax_value = value
                chosen_path = path

    return minimax_value, chosen_path + [node]

class TestMinimax(unittest.TestCase):
    def test_minimax(self):
        tree_graph = [
            [1, 2],
            [3, 4],
            [5, 6],
            [],
            [],
            [],
            []
        ]
        values = [0, 0, 0, 7, 2, 4, 9]

        expected_minimax_value = 4
        expected_path = [5, 2, 0]
        minimax_value, path = minimax(tree_graph, values, 0)
        self.assertEqual(minimax_value, expected_minimax_value)
        self.assertEqual(path, expected_path)