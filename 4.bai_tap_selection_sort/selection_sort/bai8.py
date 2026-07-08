def tim_chi_so_nho_nhat(arr, start):

    min_index = start

    for i in range(start + 1, len(arr)):

        if arr[i] < arr[min_index]:
            min_index = i

    return min_index


arr = [9, 3, 7, 1, 5]

print(tim_chi_so_nho_nhat(arr, 1))