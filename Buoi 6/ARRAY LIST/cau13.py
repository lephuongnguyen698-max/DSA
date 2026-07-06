class MyArrayList:
    def __init__(self):
        self.data = []

    def merge_intervals(self):
        self.data.sort()

        result = [self.data[0]]

        for start, end in self.data[1:]:
            if start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])

        self.data = result


arr = MyArrayList()

arr.data = [[1, 3], [2, 6], [8, 10]]

print("Ban đầu:", arr.data)

arr.merge_intervals()

print("Sau khi gộp:", arr.data)