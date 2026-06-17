def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [60,32,15,12,52,71,90,-1,-10,-30,-155,75]

bubble_sort(arr)

print(arr)
