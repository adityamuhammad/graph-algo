#
#                 1
#               /   \
#              /     \
#             /       \ w=5
#       w=2  /         \
#           /  w=6      \ 
#           0 ----2------ 4
#            \    | w=1
#        w=3  \   |
#              \  |w=2
#               \ |
#                \| 
#                 3
#
 
def dijkstra(a, b, nodes, n):
    dist = [float('inf')] * n
    visited = [False] * n
    pred = [-1] * n
    dist[a] = 0

    while True:
        u = -1
        min_dist = float('inf')
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                u = i
                min_dist = dist[i]
         
        if (u == -1 or dist[u] == float('inf')):
            break

        visited[u] = True
        for v in nodes[u]:
            w = weight(v[0], nodes[u])
            if dist[v[0]] > dist[u] + w:
                dist[v[0]] = dist[u] + w
                pred[v[0]] = u

    return dist
             
 
def weight(b, from_nodes):
    for i in from_nodes: 
        if i[0] == b: 
            return i[1]



nodes = [
    [(1,2),(2,6),(3,3)],
    [(4,5)],
    [(4,1)],
    [(2,2)],
    []
]
print(dijkstra(0,4, nodes, len(nodes)))

