def dem_hoan_doi(arr):

    swap = 0

    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:

            arr[i], arr[min_index] = arr[min_index], arr[i]

            swap += 1

    return swap


arr = [3, 2, 1]

print(dem_hoan_doi(arr))