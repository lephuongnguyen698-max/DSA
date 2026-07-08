def lower_bound(a, x):
    left, right = 0, len(a) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] >= x:
            ans = mid
            right = mid - 1  # Thử tìm phần tử nhỏ hơn ở bên trái
        else:
            left = mid + 1
    return ans

def upper_bound(a, x):
    left, right = 0, len(a) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] > x:
            ans = mid
            right = mid - 1  # Thử tìm phần tử nhỏ hơn ở bên trái
        else:
            left = mid + 1
    return ans

# Ví dụ
a = [1, 3, 5, 7]
x = 4
print(f"lower=idx {lower_bound(a, x)}")  # Output: lower=idx 2 (số 5)