def dijkstra_co_ban(adj, source):
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

        if u == -1:
            break

        visited[u] = True

        for v, w in adj[u]:
            if not visited[v]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    return dist


adj = [
    [(1, 4), (2, 1)],
    [(3, 1), (4, 6)],
    [(1, 2), (3, 5), (4, 8)],
    [(4, 3)],
    [(5, 2)],
    []
]

ket_qua = dijkstra_co_ban(adj, 0)
print("dist =", ket_qua)