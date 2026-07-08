def binary_insertion_sort(a):
    n = len(a)
    arr = a.copy()
    for i in range(1, n):
        key = arr[i]
        
        # Tìm kiếm nhị phân vị trí chèn trong đoạn [0, i-1]
        left, right = 0, i - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
        # Vị trí chèn thích hợp là `left`
        
        # Thực hiện dịch chuyển các phần tử để tạo khoảng trống
        for j in range(i - 1, left - 1, -1):
            arr[j + 1] = arr[j]
        
        arr[left] = key
    return arr

a = [3, 2, 1]
print(f"Mảng sau sắp xếp: {binary_insertion_sort(a)}")