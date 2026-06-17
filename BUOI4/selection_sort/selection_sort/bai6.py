def dem_so_sanh(arr):

    compare = 0

    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            compare += 1

            if arr[j] < arr[min_index]:
                min_index = j

    return compare


arr = [5, 2, 4, 6, 1]

print(dem_so_sanh(arr))