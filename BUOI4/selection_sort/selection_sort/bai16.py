def sap_xep_tri_tuyet_doi(arr):

    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if abs(arr[j]) < abs(arr[min_index]):
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [-3, 1, -2, 2]

print(sap_xep_tri_tuyet_doi(arr))