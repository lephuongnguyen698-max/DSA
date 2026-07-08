import heapq

def solve_large_graph():
    # Giả lập dữ liệu đồ thị thưa lớn
    n = 6 
    edges = [(0, 1, 7), (0, 2, 9), (0, 5, 14), (1, 2, 10), (1, 3, 15), (2, 3, 11), (2, 5, 2), (3, 4, 6), (5, 4, 9)]
    start_node = 0
    
    graph = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w)) # Đồ thị vô hướng
        
    dist = [float('inf')] * n
    dist[start_node] = 0
    pq = [(0, start_node)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > dist[u]: 
            continue
            
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
                
    print("Khoảng cách đồ thị lớn:", dist)

solve_large_graph()