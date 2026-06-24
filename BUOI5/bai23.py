import heapq


def tong_khoang_cach(adj, source):

    n = len(adj)

    dist = [float("inf")] * n

    dist[source] = 0

    pq = []

    heapq.heappush(pq, (0, source))

    while pq:

        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, w in adj[u]:

            if dist[u] + w < dist[v]:

                dist[v] = dist[u] + w

                heapq.heappush(pq, (dist[v], v))

    tong = 0

    for x in dist:

        if x != float("inf"):

            tong += x

    return tong


adj = [

[(1,4),(2,1)],
[(3,1),(4,6)],
[(1,2),(3,5),(4,8)],
[(4,3)],
[(5,2)],
[]

]

print(tong_khoang_cach(adj, 0))