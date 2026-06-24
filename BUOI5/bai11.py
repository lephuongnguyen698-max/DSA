import heapq


def dijkstra_nhieu_nguon(adj, sources):

    n = len(adj)
    dist = [float("inf")] * n
    pq = []
    for s in sources:

        dist[s] = 0

        heapq.heappush(pq, (0, s))

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


adj = [

    [(1, 4), (2, 1)],
    [(3, 1), (4, 6)],
    [(1, 2), (3, 5), (4, 8)],
    [(4, 3)],
    [(5, 2)],
    []

]

sources = [0, 2]

dist = dijkstra_nhieu_nguon(adj, sources)
print(dist)