class MyArrayList:
    def __init__(self):
        self.data = []

    def index_of(self, x):
        for i in range(len(self.data)):
            if self.data[i] == x:
                return i
        return -1


arr = MyArrayList()

arr.data = [5, 3, 7]

x = int(input("Nhập số cần tìm: "))

print("Danh sách:", arr.data)
print("Vị trí:", arr.index_of(x))