import heapq


def tim_khong_toi_duoc(adj, source):

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

    ds = []

    for i in range(n):

        if dist[i] == float("inf"):

            ds.append(i)

    return dist, ds


adj = [

    [(1, 4), (2, 1)],
    [(3, 1), (4, 6)],
    [(1, 2), (3, 5), (4, 8)],
    [(4, 3)],
    [(5, 2)],
    []

]

dist, ds = tim_khong_toi_duoc(adj, 0)

print(dist)

print(ds)