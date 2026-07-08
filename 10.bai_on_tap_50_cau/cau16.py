import heapq

def dijkstra_path(n, edges, start_node, target_node):
    graph = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))
        
    dist = [float('inf')] * n
    dist[start_node] = 0
    
    # Mảng lưu vết đỉnh cha
    parent = [-1] * n
    pq = [(0, start_node)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]: continue
            
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u  # Lưu lại u là đỉnh đi trước v
                heapq.heappush(pq, (dist[v], v))
                
    # Truy vết ngược từ target về start
    path = []
    curr = target_node
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    
    return " -> ".join(map(str, path))

# Ví dụ mẫu
n = 5
edges = [(0, 1, 4), (0, 2, 2), (2, 1, 1), (1, 3, 2), (2, 4, 4), (3, 4, 1)]
print("Đường đi:", dijkstra_path(n, edges, 0, 4))