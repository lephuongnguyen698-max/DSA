import heapq

def shortest_path_grid(grid):
    rows, cols = len(grid), len(grid[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = grid[0][0]
    
    # Heap lưu: (tổng_chi_phí, hàng, cột)
    pq = [(grid[0][0], 0, 0)]
    
    # Hướng đi: Lên, Xuống, Trái, Phải
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while pq:
        cost, r, c = heapq.heappop(pq)
        
        if r == rows - 1 and c == cols - 1:
            return cost
            
        if cost > dist[r][c]: 
            continue
            
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < rows and 0 <= nc < cols:
                if dist[r][c] + grid[nr][nc] < dist[nr][nc]:
                    dist[nr][nc] = dist[r][c] + grid[nr][nc]
                    heapq.heappush(pq, (dist[nr][nc], nr, nc))
    return -1

# Ví dụ lưới chi phí
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print("Chi phí nhỏ nhất trên lưới:", shortest_path_grid(grid))