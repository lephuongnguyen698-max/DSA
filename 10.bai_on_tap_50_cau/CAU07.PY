def bubble_sort_with_swaps(a):
    n = len(a)
    arr = a.copy()
    swap_count = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
    return arr, swap_count

# Ví dụ
a = [2, 3, 1]
_, swaps = bubble_sort_with_swaps(a)
print(f"Số swap: {swaps}")  # Output: 2