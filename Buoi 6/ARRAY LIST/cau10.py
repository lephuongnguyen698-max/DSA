class MyArrayList:
    def __init__(self):
        self.data = []

    def merge(self, other):
        result = []
        i = 0
        j = 0

        while i < len(self.data) and j < len(other.data):
            if self.data[i] < other.data[j]:
                result.append(self.data[i])
                i += 1
            else:
                result.append(other.data[j])
                j += 1

        while i < len(self.data):
            result.append(self.data[i])
            i += 1

        while j < len(other.data):
            result.append(other.data[j])
            j += 1

        return result


arr1 = MyArrayList()
arr2 = MyArrayList()

arr1.data = [1, 3, 5]
arr2.data = [2, 4]

print("Danh sách 1:", arr1.data)
print("Danh sách 2:", arr2.data)

merged = arr1.merge(arr2)

print("Sau khi trộn:", merged)