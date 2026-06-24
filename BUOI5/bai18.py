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


def dinh_nhieu_lang_gieng_nhat(adj, D):

    n = len(adj)

    best = -1
    so_luong = -1

    for s in range(n):

        dist = dijkstra(adj, s)

        dem = 0

        for x in dist:

            if x <= D:
                dem += 1

        if dem > so_luong:

            so_luong = dem

            best = s

    return best, so_luong


adj = [

    [(1, 4), (2, 1)],
    [(3, 1), (4, 6)],
    [(1, 2), (3, 5), (4, 8)],
    [(4, 3)],
    [(5, 2)],
    []

]

D = 4

dinh, sl = dinh_nhieu_lang_gieng_nhat(adj, D)

print(dinh)

print(sl)