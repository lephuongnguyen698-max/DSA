class MyArrayList:
    def __init__(self):
        self.data = [0] * 2
        self.size = 0

    def append(self, x):
        if self.size == len(self.data):
            new = [0] * (len(self.data) * 2)
            for i in range(self.size):
                new[i] = self.data[i]
            self.data = new

        self.data[self.size] = x
        self.size += 1

    def print_list(self):
        print(self.data[:self.size])


arr = MyArrayList()

n = int(input("Nhập số phần tử: "))

for i in range(n):
    arr.append(int(input()))

arr.print_list()