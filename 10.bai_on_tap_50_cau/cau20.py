import heapq

def heuristic(p1, p2):
    # Khoảng cách Manhattan h(n) giữa ô hiện tại và ô đích
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def a_star_search(grid, start, target):
    rows, cols = len(grid), len(grid[0])
    
    # g_score[r][c] lưu chi phí thực tế từ start đến (r, c)
    g_score = [[float('inf')] * cols for _ in range(rows)]
    g_score[start[0]][start[1]] = 0
    
    # Heap lưu: (f_score, r, c) với f_score = g_score + h_score
    pq = [(heuristic(start, target), start[0], start[1])]
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    nodes_visited = 0 # Đếm số ô phải mở rộng để so sánh độ hiệu quả
    
    while pq:
        f, r, c = heapq.heappop(pq)
        nodes_visited += 1
        
        if (r, c) == target:
            return g_score[r][c], nodes_visited
            
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < rows and 0 <= nc < cols:
                tentative_g = g_score[r][c] + grid[nr][nc]
                if tentative_g < g_score[nr][nc]:
                    g_score[nr][nc] = tentative_g
                    f_score = tentative_g + heuristic((nr, nc), target)
                    heapq.heappush(pq, (f_score, nr, nc))
                    
    return -1, nodes_visited

# Thử nghiệm so sánh định hướng mục tiêu
grid = [[1]*10 for _ in range(10)] # Lưới 10x10 toàn số 1
cost, visited = a_star_search(grid, (0, 0), (9, 9))
print(f"A* - Chi phí: {cost}, Số ô phải duyệt: {visited}")