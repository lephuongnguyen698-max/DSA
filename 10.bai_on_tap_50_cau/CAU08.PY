def bubble_sort_optimized(a):
    n = len(a)
    arr = a.copy()
    passes = 0
    for i in range(n):
        swapped = False
        passes += 1
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Nếu đi qua một lượt mà không có swap nào -> mảng đã xếp xong
        if not swapped:
            break
    return arr, passes

# Ví dụ
a = [1, 2, 3, 4]
_, total_passes = bubble_sort_optimized(a)
print(f"Số lượt: {total_passes}")  # Output: 1