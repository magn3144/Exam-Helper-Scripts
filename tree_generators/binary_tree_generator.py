def binary_tree_adj_list(num_leafs):
    adj_list = []
    nodes = 2 * num_leafs - 1
    for i in range(nodes):
        if i < nodes // 2:
            adj_list.append([2 * i + 1, 2 * i + 2])
        else:
            adj_list.append([])
    return adj_list

# Test
# num_leafs = 8
# print(binary_tree_adj_list(num_leafs))
# Output: [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [], [], [], [], []]