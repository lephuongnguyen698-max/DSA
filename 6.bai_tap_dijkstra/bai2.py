def dijkstra_chay_tay(adj, source):

    n = len(adj)

    dist = [float("inf")] * n
    visited = [False] * n

    dist[source] = 0

    thu_tu = []

    print("Vòng | Chốt | dist[]")
    print("-" * 40)

    for vong in range(n):

        u = -1

        for i in range(n):
            if not visited[i] and (
                u == -1 or dist[i] < dist[u]
            ):
                u = i

        visited[u] = True
        thu_tu.append(u)

        for v, w in adj[u]:

            if not visited[v]:

                if dist[u] + w < dist[v]:

                    dist[v] = dist[u] + w

        hien = []

        for x in dist:

            if x == float("inf"):
                hien.append("∞")
            else:
                hien.append(x)

        print(vong + 1, " | ", u, " | ", hien)

    print("\nThứ tự chốt:")
    print(*thu_tu)


adj = [
    [(1, 4), (2, 1)],
    [(3, 1), (4, 6)],
    [(1, 2), (3, 5), (4, 8)],
    [(4, 3)],
    [(5, 2)],
    []
]

dijkstra_chay_tay(adj, 0)