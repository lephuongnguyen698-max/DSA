class MyArrayList:
    def __init__(self):
        self.data = []
        self.mod_count = 0

    def add(self, x):
        self.data.append(x)
        self.mod_count += 1

    def __iter__(self):
        expected = self.mod_count

        for x in self.data:
            if expected != self.mod_count:
                raise RuntimeError("Danh sách đã bị sửa đổi!")
            yield x


arr = MyArrayList()

arr.add(1)
arr.add(2)
arr.add(3)

try:
    for x in arr:
        print(x)
        if x == 2:
            arr.add(4)
except RuntimeError as e:
    print(e)