def dijkstra_hai_dinh(adj, s, t):

    n = len(adj)

    dist = [float("inf")] * n
    visited = [False] * n

    dist[s] = 0

    while True:

        u = -1

        for i in range(n):

            if not visited[i]:

                if u == -1 or dist[i] < dist[u]:

                    u = i

        if u == -1:
            break

        visited[u] = True

        # Dừng sớm
        if u == t:
            break

        for v, w in adj[u]:

            if not visited[v]:

                if dist[u] + w < dist[v]:

                    dist[v] = dist[u] + w

    return dist[t]


adj = [

    [(1, 4), (2, 1)],
    [(3, 1), (4, 6)],
    [(1, 2), (3, 5), (4, 8)],
    [(4, 3)],
    [(5, 2)],
    []

]

s = 0
t = 4

ket_qua = dijkstra_hai_dinh(adj, s, t)

print("Khoảng cách =", ket_qua)