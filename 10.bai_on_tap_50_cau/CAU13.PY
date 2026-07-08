def count_inversions_by_merge_sort(arr):
    def merge_and_count(a, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            
            # Đếm nghịch thế ở nửa trái, nửa phải và khi gộp
            inv_count += merge_and_count(a, temp_arr, left, mid)
            inv_count += merge_and_count(a, temp_arr, mid + 1, right)
            inv_count += merge(a, temp_arr, left, mid, right)
        return inv_count

    def merge(a, temp_arr, left, mid, right):
        i = left     # Chỉ số chạy mảng con trái
        j = mid + 1  # Chỉ số chạy mảng con phải
        k = left     # Chỉ số chạy mảng tạm
        inv_count = 0

        while i <= mid and j <= right:
            if a[i] <= a[j]:
                temp_arr[k] = a[i]
                i += 1
            else:
                temp_arr[k] = a[j]
                # Nếu a[i] > a[j], thì tất cả các phần tử từ a[i] đến a[mid] đều lớn hơn a[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1

        # Sao chép các phần tử còn lại
        while i <= mid:
            temp_arr[k] = a[i]
            i += 1
            k += 1
        while j <= right:
            temp_arr[k] = a[j]
            j += 1
            k += 1

        for loop_var in range(left, right + 1):
            a[loop_var] = temp_arr[loop_var]
            
        return inv_count

    temp = [0] * len(arr)
    return merge_and_count(arr.copy(), temp, 0, len(arr) - 1)

# Ví dụ
a = [1, 20, 6, 4, 5]
print(f"Số nghịch thế: {count_inversions_by_merge_sort(a)}")  # Output: 5