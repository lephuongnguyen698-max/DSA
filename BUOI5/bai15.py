import heapq


def dijkstra(adj, source):

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

                heapq.heappush(pq, (new_dist, v))

    return dist


def tim_tam_do_thi(adj):

    n = len(adj)

    tam = -1

    ban_kinh = float("inf")

    for s in range(n):

        dist = dijkstra(adj, s)

        ecc = max(x for x in dist if x != float("inf"))

        if ecc < ban_kinh:

            ban_kinh = ecc

            tam = s

    return tam, ban_kinh


adj = [

    [(1, 4), (2, 1)],
    [(3, 1), (4, 6)],
    [(1, 2), (3, 5), (4, 8)],
    [(4, 3)],
    [(5, 2)],
    []

]

tam, bk = (tim_tam_do_thi(adj))

print("Tâm =", tam)
print("Bán kính =", bk)