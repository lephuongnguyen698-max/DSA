class MyArrayList:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def get(self, i):
        return self.data[i]

    def set(self, i, x):
        self.data[i] = x

    def size(self):
        return len(self.data)


if __name__ == "__main__":
    arr = MyArrayList()

    arr.add(1)
    arr.add(2)
    arr.add(3)

    print(arr.get(1))
    arr.set(1, 10)
    print(arr.data)
    print(arr.size())