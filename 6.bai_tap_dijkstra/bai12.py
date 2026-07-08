import heapq


def dem_so_duong_di_ngan_nhat(adj, source):

    n = len(adj)
    dist = [float("inf")] * n
    count = [0] * n
    dist[source] = 0
    count[source] = 1
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
                count[v] = count[u]

                heapq.heappush(pq, (new_dist, v))

            elif new_dist == dist[v]:

                count[v] += count[u]

    return dist, count


adj = [

    [(1, 4), (2, 1)],
    [(3, 1), (4, 6)],
    [(1, 2), (3, 5), (4, 8)],
    [(4, 3)],
    [(5, 2)],
    []

]

dist, count = dem_so_duong_di_ngan_nhat(
    adj,
    0
)

print("dist =", dist)

print("count =", count)