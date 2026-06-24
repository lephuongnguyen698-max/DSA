import heapq


def dijkstra(adj, source):

    n = len(adj)

    dist = [float("inf")] * n

    dist[source] = 0

    pq = []

    heapq.heappush(pq, (0, source))

    while pq:

        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, w in adj[u]:

            new_dist = dist[u] + w

            if new_dist < dist[v]:

                dist[v] = new_dist

                heapq.heappush(pq, (new_dist, v))

    return dist


def duong_kinh_do_thi(adj):

    n = len(adj)

    diameter = 0

    cap = ()

    for s in range(n):

        dist = dijkstra(adj, s)

        for t in range(n):

            if dist[t] != float("inf"):

                if dist[t] > diameter:

                    diameter = dist[t]

                    cap = (s, t)

    return diameter, cap


adj = [

    [(1, 4), (2, 1)],
    [(3, 1), (4, 6)],
    [(1, 2), (3, 5), (4, 8)],
    [(4, 3)],
    [(5, 2)],
    []

]

dk, cap = duong_kinh_do_thi(adj)

print(dk)

print(cap)