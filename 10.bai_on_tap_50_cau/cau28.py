from collections import deque

def bfs_by_layers(graph, start):
    visited = {start}
    queue = deque([start])
    order = []
    
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
    return order

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}
print(bfs_by_layers(graph, 0))