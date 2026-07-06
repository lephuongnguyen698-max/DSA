class MyArrayList:
    def __init__(self):
        self.data = []

    def insert(self, index, value):
        self.data.insert(index, value)

    def remove(self, index):
        self.data.pop(index)


if __name__ == "__main__":
    arr = MyArrayList()

    arr.data = [1, 2, 4]

    arr.insert(2, 3)
    print(arr.data)

    arr.remove(1)
    print(arr.data)