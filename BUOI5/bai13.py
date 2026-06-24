import heapq


def dijkstra_gioi_han_canh( adj, source, K):

    n = len(adj)
    dist = [float("inf")] * n
    pq = []
    dist[source] = 0

    heapq.heappush(pq, (0, source, 0))

    while pq:

        current_dist, u, steps = (heapq.heappop(pq))

        if current_dist > dist[u]:
            continue

        if steps == K:
            continue

        for v, w in adj[u]:

            new_dist = (dist[u] + w)

            if new_dist < dist[v]:

                dist[v] = new_dist

                heapq.heappush(pq, (new_dist, v, steps + 1))

    return dist


adj = [

    [(1, 4), (2, 1)],
    [(3, 1), (4, 6)],
    [(1, 2), (3, 5), (4, 8)],
    [(4, 3)],
    [(5, 2)],
    []

]

K = 3
dist = dijkstra_gioi_han_canh(adj,0, K)

print(dist)