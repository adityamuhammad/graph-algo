def dfs_recursive(curr_node):
    visited[curr_node] = True
    for adj_node in adj[curr_node]:
        if not visited[adj_node]:
            dfs_recursive(adj_node)


visited = [False] * 4
adj = [
    [2,2,3],
    [3],
    [3],
    [1],
]

visited = [False] * 4
adj = [
    [1,2,3],
    [0],
    [3],
    [1]
]

dfs_recursive(0)
