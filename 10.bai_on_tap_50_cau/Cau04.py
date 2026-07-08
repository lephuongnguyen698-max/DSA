def search_rotated_array(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        
        # Kiểm tra xem nửa bên trái có được sắp xếp tăng dần hoàn chỉnh không
        if a[left] <= a[mid]:
            # Nếu x nằm trong khoảng của nửa trái
            if a[left] <= x < a[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Ngược lại, nửa bên phải chắc chắn được sắp xếp hoàn chỉnh
        else:
            # Nếu x nằm trong khoảng của nửa phải
            if a[mid] < x <= a[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# Ví dụ
a = [4, 5, 6, 7, 0, 1, 2]
x = 0
print(f"Chỉ số: {search_rotated_array(a, x)}")  # Output: 4