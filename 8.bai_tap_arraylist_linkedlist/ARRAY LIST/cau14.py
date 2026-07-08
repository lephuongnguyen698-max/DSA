class Matrix:
    def __init__(self):
        self.data = []

    def add_row(self, row):
        self.data.append(row)

    def set(self, i, j, value):
        self.data[i][j] = value

    def get(self, i, j):
        return self.data[i][j]


m = Matrix()

m.add_row([1, 2, 3])
m.add_row([4, 5, 6])

print("Ma trận:")
for row in m.data:
    print(row)

m.set(1, 2, 100)

print("Sau khi sửa:")
for row in m.data:
    print(row)

print("get(1,2) =", m.get(1, 2))