def test_empty_matrix():
    assert mat_to_list([]) == []

def test_single_node_no_edges():
    assert mat_to_list([[0]]) == [[]]

def test_simple_graph():
    adj_mat = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    expected_adj_list = [[1], [0, 2], [1]]
    assert mat_to_list(adj_mat) == expected_adj_list

# test_empty_matrix()
# test_single_node_no_edges()
# test_simple_graph()