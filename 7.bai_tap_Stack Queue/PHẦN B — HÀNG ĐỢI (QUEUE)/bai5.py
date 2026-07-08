class HangDoi:

    def __init__(self):
        self.mang = []

    def them(self, gia_tri):
        self.mang.append(gia_tri)

    def front(self):
        return self.mang[0]

    def rear(self):
        return self.mang[-1]


q = HangDoi()

q.them(4)
q.them(5)
q.them(6)

print("Front:", q.front())

print("Rear:", q.rear())