def reachable(adj_list, start_node):
    """ Compute the nodes reachable from a start node

    For the above example, reachable([[1, 3], [2], [0], [4], [3], []], 0)) must return {0, 1, 2, 3, 4}
    and reachable([[1, 3], [2], [0], [4], [3], []], 3) must return {3, 4}

    Parameters:
    -----------
    adj_list : the adjacency list of the graph
    start_node: the index of the start node

    Returns:
    --------
    reachable: set(int) the set of nodes reachable from start_node


    """

    final_result = set()
    stack = [start_node]  

    while stack: # while the stack is not empty this while loop will keep executing
        node = stack.pop() # pops the last element
        if node not in final_result:
            final_result.add(node)
            stack.extend(adj_list[node]) # adding the new fetched list to the stack to keep checking on further levels
     
    return final_result