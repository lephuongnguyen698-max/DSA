def dem_so_sanh(arr):

    compare = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            compare += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break

        arr[j + 1] = key

    return compare


arr = [1, 2, 3]
print(dem_so_sanh(arr))