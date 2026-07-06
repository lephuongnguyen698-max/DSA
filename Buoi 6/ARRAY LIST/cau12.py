class MyArrayList:
    def __init__(self):
        self.data = []

    def remove_duplicate(self):
        seen = set()
        result = []

        for x in self.data:
            if x not in seen:
                seen.add(x)
                result.append(x)

        self.data = result


arr = MyArrayList()
arr.data = [3, 1, 3, 2, 1]

print("Ban đầu:", arr.data)

arr.remove_duplicate()

print("Sau khi xóa:", arr.data)