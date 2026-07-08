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


def tram_trung_chuyen(adj):

    n = len(adj)

    best = -1

    tong_nho_nhat = float("inf")

    for s in range(n):

        dist = dijkstra(adj, s)

        tong = 0

        for x in dist:

            if x != float("inf"):

                tong += x

        if tong < tong_nho_nhat:

            tong_nho_nhat = tong

            best = s

    return best, tong_nho_nhat


adj = [

    [(1, 4), (2, 1)],
    [(3, 1), (4, 6)],
    [(1, 2), (3, 5), (4, 8)],
    [(4, 3)],
    [(5, 2)],
    []

]

dinh, tong = tram_trung_chuyen(adj)

print(dinh)

print(tong)