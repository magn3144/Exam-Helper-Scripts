import copy


def seperate_graph_and_costs(weighted_graph):
    """Seperate a weighted graph into a graph and a dictionary of weights
    
    Arguments:
        weighted_graph {list} -- List of lists of tuples containing the weighted graph as an adjacency list,
        where each tuple contains the node and the weight of the edge as integers
    
    Returns:
        graph {list} -- Adjacency list containing the graph
        weights {dict} -- Dictionary containing the weights
    """

    # Initialize the graph and the weights
    graph = []
    weights = {}

    # Iterate through the nodes and edges of the weighted graph
    for i, node in enumerate(weighted_graph):
        graph.append([])
        for connected_node in node:
            graph[-1].append(connected_node[0])
            weights[(i, connected_node[0])] = connected_node[1]
    
    return graph, weights

def convert_graph_to_undirected(graph, costs = None):
    # Add the reverse edges to the graph, so that the graph is undirected
    # Also add the reverse edges to the costs dictionary
    for i, connected_nodes in enumerate(graph):
        for connected_node in connected_nodes:
            if i not in graph[connected_node]:
                graph[connected_node].append(i)
                if costs != None:
                    costs[(connected_node, i)] = costs[(i, connected_node)]
    
    return graph, costs

def add_costs_to_graph(graph, cost):
    _graph = copy.deepcopy(graph)
    for i in range(len(_graph)):
        for j in range(len(_graph[i])):
            _graph[i][j] = (_graph[i][j], cost)
    return _graph