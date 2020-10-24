def one_is_subset(a, b):
    if a.__sizeof__() > 1 and b.__sizeof__() > 1:
        return -1

    if a.__sizeof__() == 1 and b.__sizeof__() == 1:
        return -1

    if a.issubset(b):
        return 0

    if b.issubset(a):
        return 1

    return -1


def apply_arc_consistency(nodes, nodes_sets, edges):
    flag = True

    while flag:
        flag = False

        for edge in edges:
            result = one_is_subset(set(nodes_sets[edge[0]]), set(nodes_sets[edge[1]]))
            if result != -1:
                a = edge[1 - result]
                b = edge[result]
                new_set = set(nodes_sets[a]) - set(nodes_sets[b])
                nodes_sets[a] = list(new_set)
                flag = True


nodes = [1, 2, 3, 4]
node_sets = [[1, 2], [1, 2], [1, 2, 3], [1, 2, 3, 4]]
edges = [(0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (2, 3)]
apply_arc_consistency(nodes, node_sets, edges)

print(node_sets)