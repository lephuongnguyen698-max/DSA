class MyArrayList:
    def __init__(self):
        self.data = [0] * 2
        self.size = 0

    def add(self, x):
        if self.size == len(self.data):
            new = [0] * (len(self.data) * 2)
            for i in range(self.size):
                new[i] = self.data[i]
            self.data = new
            print("Đã mở rộng lên", len(self.data))

        self.data[self.size] = x
        self.size += 1

    def print_list(self):
        print(self.data[:self.size])


arr = MyArrayList()

for i in range(1, 6):
    arr.add(i)

arr.print_list()