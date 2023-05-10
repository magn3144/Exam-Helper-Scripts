from tools.tools import seperate_graph_and_costs, convert_graph_to_undirected, add_costs_to_graph


def calculate_optimal_costs(graph, costs, goal_node):
    """Calculate the optimal cost from each node to the goal node in the graph
    
    Arguments:
        graph {list} -- Directed graph represented as an adjacency list
        costs {dict} -- Dictionary containing the cost of each edge
        goal_node {int} -- Goal node
    
    Returns:
        costs_to_goal {dict} -- Dictionary containing the optimal cost from each node in the graph to the goal node
    """

    graph, costs = convert_graph_to_undirected(graph, costs)

    # Initialize the cost to reach the goal node from each node to infinity
    # except for the goal node itself, which has a cost of 0
    costs_to_goal = {node: float('inf') for node in range(len(graph))}
    costs_to_goal[goal_node] = 0

    # Create a priority queue of nodes to explore, starting with the goal node
    # and with a priority equal to the cost to reach that node from the goal node
    nodes_to_explore = [(goal_node, 0)]

    # Keep track of the nodes that have already been explored
    explored_nodes = set()

    # Explore the graph until all nodes have been explored
    while nodes_to_explore:
        # Get the node with the lowest priority from the priority queue
        current_node, current_cost = nodes_to_explore.pop(0)

        # If the node has already been explored, skip it
        if current_node in explored_nodes:
            continue

        # Update the cost to reach each neighbor of the current node
        for neighbor_node in graph[current_node]:
            # Calculate the cost to reach the neighbor node from the current node
            neighbor_cost = current_cost + costs[(current_node, neighbor_node)]

            # If the new cost is lower than the current cost to reach the neighbor node,
            # update the cost and add the neighbor node to the priority queue
            if neighbor_cost < costs_to_goal[neighbor_node]:
                costs_to_goal[neighbor_node] = neighbor_cost
                nodes_to_explore.append((neighbor_node, neighbor_cost))

        # Mark the current node as explored
        explored_nodes.add(current_node)

    return costs_to_goal

def is_admissible(graph, goal_node, h_values, costs = None):
    """Checks if the heuristic is admissible
    
    Arguments:
        graph {list} -- Graph represented as an adjacency list
        goal_node {int} -- Goal node
        h_values {dict} -- Dictionary containing heuristic values for each node
        costs {dict} -- Dictionary containing the cost of each edge
    
    Returns:
        is_admissible {bool} -- True if the heuristic is admissible, False otherwise
    """

    if type(costs) == int:
        graph = add_costs_to_graph(graph, costs)
        costs = None
    if costs is None:
        graph, costs = seperate_graph_and_costs(graph)
    optimal_costs = calculate_optimal_costs(graph, costs, goal_node)
    is_admissible = True
    for node in range(len(graph)):
        if h_values[node] > optimal_costs[node]:
            is_admissible = False
            break
    return is_admissible

def is_consistent(graph, h_values, costs = None):
    """Checks if the heuristic is consistent
    
    Arguments:
        graph {list} -- Graph represented as an adjacency list
        h_values {dict} -- Dictionary containing heuristic values for each node
        costs {dict} -- Dictionary containing the cost of each edge
    
    Returns:
        is_consistent {bool} -- True if the heuristic is consistent, False otherwise
    """
    
    if type(costs) == int:
        graph = add_costs_to_graph(graph, costs)
        costs = None
    if costs is None:
        graph, costs = seperate_graph_and_costs(graph)

    is_consistent = True
    for n in range(len(graph)):
        for m in graph[n]:
            if h_values[n] > costs[(n,m)] + h_values[m]:
                is_consistent = False
                break
    return is_consistent