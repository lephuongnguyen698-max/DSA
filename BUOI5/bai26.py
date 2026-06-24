import heapq

def lien_thong(adj, source):
    
    n = len(adj)
    
    dist = [float("inf")] * n
    dist[source] = 0
    pq = []
    
    heapq.heappush(pq, (0 source))
    
    for i in range(n):
        dist[i] = adj[i]
        
        return dist
    
    