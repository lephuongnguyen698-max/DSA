def bellman_ford(n, edges, start_node):
    dist = [float('inf')] * n
    dist[start_node] = 0
    
    # Lặp V - 1 lần
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                
    # Kiểm tra chu trình âm
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return "Đồ thị chứa chu trình âm!"
            
    return dist

# Ví dụ đồ thị có cạnh âm nhưng không có chu trình âm
n = 3
edges = [(0, 1, 3), (0, 2, 5), (2, 1, -4)] # 0 -> 2 -> 1 tốt hơn 0 -> 1
print("Kết quả Bellman-Ford:", bellman_ford(n, edges, 0))