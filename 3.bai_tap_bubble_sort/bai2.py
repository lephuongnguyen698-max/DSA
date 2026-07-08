def bubble_sort_tang_dan(arr):
    n = len(arr)
    for i in range(n):

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

a = [5, 1, 4, 2, 8]
bubble_sort_tang_dan(a)

print("Mảng sau khi sắp xếp tăng dần:")
print(a)