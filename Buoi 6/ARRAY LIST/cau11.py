class MyArrayList:
    def __init__(self):
        self.data = []

    def reverse(self, left, right):
        while left < right:
            self.data[left], self.data[right] = self.data[right], self.data[left]
            left += 1
            right -= 1

    def rotate(self, k):
        n = len(self.data)
        if n == 0:
            return

        k %= n

        self.reverse(0, n - 1)
        self.reverse(0, k - 1)
        self.reverse(k, n - 1)


arr = MyArrayList()
arr.data = [1, 2, 3, 4, 5]

k = int(input("Nhập k: "))

print("Ban đầu:", arr.data)
arr.rotate(k)
print("Sau khi xoay:", arr.data)