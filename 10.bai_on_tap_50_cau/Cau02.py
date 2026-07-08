def find_first_last_count(a, x):
    # Tìm vị trí đầu tiên
    def find_first():
        left, right = 0, len(a) - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] == x:
                first = mid
                right = mid - 1  # Tiếp tục tìm sang bên trái
            elif a[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return first

    # Tìm vị trí cuối cùng
    def find_last():
        left, right = 0, len(a) - 1
        last = -1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] == x:
                last = mid
                left = mid + 1  # Tiếp tục tìm sang bên phải
            elif a[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return last

    dau = find_first()
    if dau == -1:
        return f"Không tìm thấy {x}"
    
    cuoi = find_last()
    dem = cuoi - dau + 1
    return f"đầu={dau}, cuối={cuoi}, đếm={dem}"

# Ví dụ
a = [1, 2, 2, 2, 3]
x = 2
print(find_first_last_count(a, x))  # Output: đầu=1, cuối=3, đếm=3