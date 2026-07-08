from collections import deque

q = deque()
q.append('data analytics')      # Thêm phần tử vào cuối queue
q.append('data structures and algorithms')      
q.append('big data')
q.append('learning data analytics')

print(q)
print(q.popleft())         # Lấy và xóa phần tử đầu tiên trong Queue rồi in ra màn hình
print(q.popleft())         
print(q)