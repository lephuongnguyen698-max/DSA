def sap_xep_k_phan_tu(arr, k):

    for i in range(k):

        min_index = i

        for j in range(i + 1, len(arr)):

            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [5, 3, 1, 4, 2]

print(sap_xep_k_phan_tu(arr, 2))