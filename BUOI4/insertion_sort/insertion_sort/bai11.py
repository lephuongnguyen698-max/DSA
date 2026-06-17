def sap_xep_tri_tuyet_doi(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and abs(arr[j]) > abs(key):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


arr = [-3, 1, -2, 2]

print(sap_xep_tri_tuyet_doi(arr))