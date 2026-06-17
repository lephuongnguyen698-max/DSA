def dem_swap_thuc_te(arr):

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


arr = [1, 2, 3]

print(dem_swap_thuc_te(arr))