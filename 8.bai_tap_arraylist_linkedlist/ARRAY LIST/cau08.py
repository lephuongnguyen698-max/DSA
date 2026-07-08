class MyArrayList:
    def __init__(self):
        self.data = []

    def remove_even(self):
        i = 0
        while i < len(self.data):
            if self.data[i] % 2 == 0:
                self.data.pop(i)
            else:
                i += 1


arr = MyArrayList()

arr.data = [1, 2, 3, 4]

print("Ban đầu:", arr.data)

arr.remove_even()

print("Sau khi xóa:", arr.data)