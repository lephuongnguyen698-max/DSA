def sap_xep_hoc_sinh(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and (
            arr[j][1] < key[1] or
            (arr[j][1] == key[1] and arr[j][0] > key[0])
        ):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


arr = [('An', 8), ('Ba', 9), ('Cu', 8)]

print(sap_xep_hoc_sinh(arr))