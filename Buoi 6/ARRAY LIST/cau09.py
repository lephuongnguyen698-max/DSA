class MyArrayList:
    def __init__(self):
        self.data = []

    def reverse(self):
        left = 0
        right = len(self.data) - 1

        while left < right:
            self.data[left], self.data[right] = self.data[right], self.data[left]
            left += 1
            right -= 1


arr = MyArrayList()

arr.data = [1, 2, 3, 4]

print("Ban đầu:", arr.data)

arr.reverse()

print("Sau khi đảo:", arr.data)