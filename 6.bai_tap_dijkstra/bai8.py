def dem_dinh_trong_ban_kinh(adj, source, D):
    n = len(adj)
    
    dist = [float("inf")] * n
    visited = [False] * n
    
    dist[source] = 0
    
    for i in range(n):
        u = -1
        
        for i in range(n):
            if not visited[i]:
                if u == -1 or dist[i] < dist[u]:
                    u = 1
                    
        visited[u] = True
        
        for v, w in adj[u]:
            if not visited[v]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    dem = 0

    cac_dinh = []

    for i in range(n):

        if dist[i] <= D:

            dem += 1

            cac_dinh.append(i)

    return dem, cac_dinh, dist


adj = [

    [(1, 4), (2, 1)],
    [(3, 1), (4, 6)],
    [(1, 2), (3, 5), (4, 8)],
    [(4, 3)],
    [(5, 2)],
    []

]

D = 3

so_dinh, ds, dist = dem_dinh_trong_ban_kinh(adj, 0, D)

print("dist =", dist)

print("Các đỉnh =", ds)

print("Số đỉnh =", so_dinh)
                 