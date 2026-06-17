def sap_xep_hoc_sinh(arr):

    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if arr[j][1] < arr[min_index][1]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [('An', 8), ('Ba', 5)]

print(sap_xep_hoc_sinh(arr))