def insertion_sort_with_shifts(a):
    n = len(a)
    arr = a.copy()
    shift_count = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Thực hiện 1 phép dịch chuyển (shift)
            shift_count += 1
            j -= 1
        arr[j + 1] = key
    return arr, shift_count

# Ví dụ
a = [3, 2, 1]
_, shifts = insertion_sort_with_shifts(a)
print(f"Số shift: {shifts}")  # Output: 3