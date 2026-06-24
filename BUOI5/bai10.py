def chon_dijkstra(V, E):

    if E > V * V / 10:

        return "Dùng Dijkstra O(V²)"

    else:

        return "Dùng Dijkstra Heap"


print(chon_dijkstra(100000, 200000))

print(chon_dijkstra(1000, 900000))