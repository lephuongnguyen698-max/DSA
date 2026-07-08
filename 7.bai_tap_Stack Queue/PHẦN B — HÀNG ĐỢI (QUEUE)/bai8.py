from collections import deque


class HangDoiHaiDau:

    def __init__(self):
        self.mang = deque()

    def them_dau(self, x):
        self.mang.appendleft(x)

    def them_cuoi(self, x):
        self.mang.append(x)

    def xoa_dau(self):
        return self.mang.popleft()

    def xoa_cuoi(self):
        return self.mang.pop()


q = HangDoiHaiDau()

q.them_dau(1)

q.them_cuoi(2)

print(q.mang)