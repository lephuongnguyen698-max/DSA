def sap_xep_ky_tu(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


arr = ['d', 'a', 'c', 'b']
print(sap_xep_ky_tu(arr))