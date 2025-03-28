def mat_to_list(adj_mat):
    """ Convert adjacency matrix to an adjacency list representation

    Parameters:
    -----------
    adj_mat : (a square 0-1 matrix)
        Adjacency matrix (n x n) of the graph (of n nodes)


    Returns:
    --------
     adj_list: `list[list[int]]`
        The adjacency list of the graph
    """

    adj_list = []
    for i in range(len(adj_mat)): # this loop runs for total no of lists in matrix
        adj_list_elements = [] 
        for j in range(len(adj_mat[i])): # running the inner loop for total no of elements in each list of adj_mat
            if(adj_mat[i][j] == 1): # where the number is 1 it takes that index and append it to adj_list_elements
                adj_list_elements.append(j)
        adj_list.append(adj_list_elements) # pushing the created list into adj_list
    return adj_list # returns adj_list