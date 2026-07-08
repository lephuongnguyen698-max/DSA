def selection_sort(a):
    n = len(a)
    arr = a.copy()
    comparison_count = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparison_count += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr, comparison_count

# Ví dụ
a = [5, 3, 1, 4, 2]
_, comps = selection_sort(a)
print(f"Số so sánh với n=5: {comps}")  # Output: 10 (vì 5*(5-1)/2 = 10)