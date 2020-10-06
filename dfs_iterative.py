def dfs_iterative(initial_node):
    stack = []
    stack.append(initial_node)
    visited[initial_node] = True
    while stack:
        curr_node = stack.pop()
        for adj_node in adj[curr_node]:
            if not visited[adj_node]:
                stack.append(adj_node)
                visited[adj_node] = True


visited = [False] * 4
adj = [
    [1,2,3],
    [0],
    [3],
    [1]
]

dfs_iterative(0)
