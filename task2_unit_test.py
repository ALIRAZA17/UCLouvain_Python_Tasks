def test_reachable_simple():
    adj_list = [[1, 3], [2], [0], [4], [3], []]
    assert reachable(adj_list, 0) == {0, 1, 2, 3, 4}

def test_reachable_from_isolated_node():
    adj_list = [[1], [2], [], [4], [3], []]
    assert reachable(adj_list, 5) == {5}

def test_reachable_from_middle():
    adj_list = [[1, 2], [3], [3, 4], [], [5], []]
    assert reachable(adj_list, 2) == {2, 3, 4, 5}


# test_reachable_simple()
# test_reachable_from_isolated_node()
# test_reachable_from_middle()