def bfs(initial_node):
    queue = []
    queue.append(initial_node)
    visited[initial_node] = True
    while queue:
        curr_node = queue.pop(0)
        print("visit", curr_node)
        for adj_node in adj[curr_node]:
            if not visited[adj_node]:
                queue.append(adj_node)
                visited[adj_node] = True


visited = [False] * 11
adj = [
    [1,2,3,4,5],
    [6,7],
    [],
    [8,9],
    [],
    [],
    [],
    [10],
    [],
    [],
    []
]

bfs(0)
