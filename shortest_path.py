def shortest_path(node_a, node_b, adj, total_node):
    queue = []
    visit_time = [-1] * total_node
    queue.append(node_a)
    visit_time[node_a] = 0

    while queue:
        curr_node = queue.pop(0)
        for adj_node in adj[curr_node]:
            if visit_time[adj_node] == -1:
                queue.append(adj_node)
                visit_time[adj_node] = visit_time[curr_node] + 1

    return visit_time[node_b]


adj = [
    [1,2,3,4,5],
    [6,7],
    [10],
    [8,9],
    [],
    [],
    [],
    [10],
    [],
    [],
    []
]
print("shortest path : ",shortest_path(0,10, adj, len(adj)))
