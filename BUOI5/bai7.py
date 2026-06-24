def dijkstra_truy_vet(adj, s, t):

    n = len(adj)

    dist = [float("inf")] * n
    visited = [False] * n
    parent = [-1] * n

    dist[s] = 0

    for i in range(n):

        u = -1

        for i in range(n):

            if not visited[i]:

                if u == -1 or dist[i] < dist[u]:

                    u = i

        visited[u] = True

        for v, w in adj[u]:

            if not visited[v]:

                if dist[u] + w < dist[v]:

                    dist[v] = dist[u] + w

                    parent[v] = u

    path = []

    cur = t

    while cur != -1:

        path.append(cur)

        cur = parent[cur]

    path.reverse()

    return dist[t], path


adj = [

    [(1, 4), (2, 1)],
    [(3, 1), (4, 6)],
    [(1, 2), (3, 5), (4, 8)],
    [(4, 3)],
    [(5, 2)],
    []

]

do_dai, duong_di = dijkstra_truy_vet(adj, 0, 4)

print("Độ dài =", do_dai)

print("Đường đi:")

print(" -> ".join(map(str, duong_di)))