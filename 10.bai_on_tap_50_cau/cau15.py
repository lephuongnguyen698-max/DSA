import heapq

def dijkstra_basic(n, edges, start_node):
    # 1. Khởi tạo danh sách kề
    graph = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))
    
    # 2. Khởi tạo mảng khoảng cách
    dist = [float('inf')] * n
    dist[start_node] = 0
    
    # 3. Hàng đợi ưu tiên (min-heap)
    pq = [(0, start_node)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > dist[u]:
            continue
            
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
                
    return dist

# Ví dụ mẫu
n = 5
edges = [(0, 1, 4), (0, 2, 2), (2, 1, 1), (1, 3, 2), (2, 4, 4), (3, 4, 1)]
s = 0
print("dist[] =", dijkstra_basic(n, edges, s))