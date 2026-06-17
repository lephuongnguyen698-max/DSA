def sap_xep_giam_dan(arr):

    n = len(arr)

    for i in range(n):

        max_index = i

        for j in range(i + 1, n):

            if arr[j] > arr[max_index]:
                max_index = j

        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr


arr = [5, 2, 4, 6, 1]

print(sap_xep_giam_dan(arr))