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
    p = [-1] * n
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
                p[v[0]] = u

    return (dist, p)
             
 
def weight(b, from_nodes):
    for i in from_nodes: 
        if i[0] == b: 
            return i[1]

def trav_path(a, b, p):
    if p[b] == -1 and b != a:
        print("there is no way")
    elif p[b] != -1:
        trav_path(a, p[b], p)
        print([p[b],b])


nodes = [
    [(1,2),(2,6),(3,3)],
    [(4,5)],
    [(4,1)],
    [(2,2)],
    []
]
dijkstra_func =dijkstra(0,4, nodes, len(nodes))
distances, paths = dijkstra_func[0], dijkstra_func[1]
print(distances)

print(trav_path(0,4, paths))
