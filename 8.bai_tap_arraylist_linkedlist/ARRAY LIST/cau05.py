class MyArrayList:
    def __init__(self):
        self.data = []

    def print_list(self):
        for x in self.data:
            print(x, end=" ")
        print()

    def count_even(self):
        count = 0
        for x in self.data:
            if x % 2 == 0:
                count += 1
        return count


arr = MyArrayList()

arr.data = [1, 2, 3, 4]

print("Danh sách:")
arr.print_list()

print("Số phần tử chẵn:", arr.count_even())