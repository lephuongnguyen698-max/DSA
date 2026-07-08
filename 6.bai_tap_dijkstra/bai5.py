def dijkstra_thanh_pho(adj, source):
    n = len(adj)

    dist = [float("inf")] * n
    visited = [False] * n

    dist[source] = 0

    for i in range(n):

        u = -1

        for j in range(n):
            if not visited[j]:
                if u == -1 or dist[j] < dist[u]:
                    u = j

        if u == -1 or dist[u] == float("inf"):
            break

        visited[u] = True

        for v, w in adj[u]:
            if not visited[v]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    return dist

adj = [
    [(1, 4), (2, 3)],          
    [(0, 4), (3, 2)],          
    [(0, 3), (3, 5)],          
    [(1, 2), (2, 5), (4, 4)],  
    [(3, 4)],                  
    []                         
]

ten = ["A", "B", "C", "D", "E", "F"]

source = 0

dist = dijkstra_thanh_pho(adj, source)

print("Khoảng cách ngắn nhất từ", ten[source])

for i in range(len(dist)):
    if dist[i] == float("inf"):
        print(ten[source], "->", ten[i], "= -1")
    else:
        print(ten[source], "->", ten[i], "=", dist[i])