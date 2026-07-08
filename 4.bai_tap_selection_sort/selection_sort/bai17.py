def phan_tu_nho_thu_k(arr, k):

    for i in range(k):

        min_index = i

        for j in range(i + 1, len(arr)):

            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr[k - 1]


arr = [7, 2, 5, 1, 9]

print(phan_tu_nho_thu_k(arr, 3))