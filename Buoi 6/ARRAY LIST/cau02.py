class MyArrayList:
    def __init__(self):
        self.data = []

    def append(self, x):
        self.data.append(x)

    def pop_back(self):
        return self.data.pop()


if __name__ == "__main__":
    arr = MyArrayList()

    arr.append(1)
    arr.append(2)
    arr.append(3)

    print(arr.data)
    print(arr.pop_back())
    print(arr.data)