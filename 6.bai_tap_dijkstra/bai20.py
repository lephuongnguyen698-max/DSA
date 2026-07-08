import heapq


def dijkstra_tranh_dinh(adj, source, cam):

    n = len(adj)

    dist = [float("inf")] * n

    dist[source] = 0

    pq = []

    heapq.heappush(pq, (0, source))

    while pq:

        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        if u == cam:
            continue

        for v, w in adj[u]:

            if v == cam:
                continue

            new_dist = dist[u] + w

            if new_dist < dist[v]:

                dist[v] = new_dist

                heapq.heappush(pq, (new_dist, v))

    return dist


adj = [

    [(1, 4), (2, 1)],
    [(3, 1), (4, 6)],
    [(1, 2), (3, 5), (4, 8)],
    [(4, 3)],
    [(5, 2)],
    []

]

cam = 3

dist = dijkstra_tranh_dinh(adj, 0, cam)

print(dist)