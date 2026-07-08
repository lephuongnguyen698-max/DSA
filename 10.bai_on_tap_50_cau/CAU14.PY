def shell_sort(a, gaps):
    arr = a.copy()
    n = len(arr)
    total_shifts = 0
    
    # Duyệt qua từng khoảng cách gap trong danh sách cấu hình
    for gap in gaps:
        # Thực hiện insertion sort cho các phần tử cách nhau khoảng 'gap'
        for i in range(gap, n):
            key = arr[i]
            j = i
            # So sánh và dịch chuyển (shift) các phần tử cách nhau 'gap' đơn vị
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                total_shifts += 1
                j -= gap
            arr[j] = key
            
    return arr, total_shifts

# Thử nghiệm với mảng mẫu và dãy gap khác nhau
a = [9, 8, 3, 7, 5, 6, 4, 1]

gap_sequence_1 = [4, 2, 1]
_, shifts_1 = shell_sort(a, gap_sequence_1)

gap_sequence_2 = [3, 1]
_, shifts_2 = shell_sort(a, gap_sequence_2)

print(f"Tổng số shift với gap [4, 2, 1]: {shifts_1}")
print(f"Tổng số shift với gap [3, 1]: {shifts_2}")