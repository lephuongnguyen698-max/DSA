import heapq


def tim_dinh_xa_nhat(adj, source):

    n = len(adj)

    dist = [float("inf")] * n

    dist[source] = 0

    pq = []

    heapq.heappush(pq, (0, source))

    while pq:

        current_dist, u = (heapq.heappop(pq))

        if current_dist > dist[u]:

            continue

        for v, w in adj[u]:

            new_dist = (dist[u] + w)

            if new_dist < dist[v]:
                dist[v] = new_dist

                heapq.heappush(pq,(new_dist, v))

    xa_nhat = -1

    khoang_cach = -1

    for i in range(n):
        if (dist[i] != float("inf") and dist[i] > khoang_cach):
            khoang_cach = dist[i]
            xa_nhat = i

    return (dist, xa_nhat, khoang_cach)


adj = [

    [(1, 4), (2, 1)],
    [(3, 1), (4, 6)],
    [(1, 2), (3, 5), (4, 8)],
    [(4, 3)],
    [(5, 2)],
    []

]

dist, dinh, kc = (tim_dinh_xa_nhat(adj, 0))

print("dist =", dist)
print("Đỉnh xa nhất =", dinh)
print("Khoảng cách =", kc)