from queue import Queue

q = Queue(maxsize=5)
print(q.qsize())

q.put('data analytics')         # Thêm phần tử vào cuối Queue
q.put('data structures and algorithms')
q.put('big data')
q.put('learning data analytics')


print(q.qsize())
print(q.get())              # Lấy và xóa phần tử đầu tiên trong Queue
print(q.get())                            