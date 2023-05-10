from search.breath_first_search import reconstruct_path
import matplotlib.pyplot as plt


def dfs(graph, start_node, goal_node):
    """Depth-first search algorithm
    
    Arguments:
        graph {list} -- Graph represented as an adjacency list
        start_node {int} -- Start node
        goal_node {int} -- Goal node
    
    Returns:
        list -- Path from start node to goal node
    """
    frontier = [start_node]
    explored = set()
    cameFrom = {}
    cameFrom[start_node] = None
    
    while frontier:
        current_node = frontier.pop()
        explored.add(current_node)
        
        if current_node == goal_node:
            return reconstruct_path(cameFrom, current_node, start_node)
        
        neighbors = graph[current_node]
        for neighbor in neighbors:
            if neighbor not in explored and neighbor not in frontier:
                cameFrom[neighbor] = current_node
                frontier.append(neighbor)
    
    return None