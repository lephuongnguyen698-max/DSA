def dem_dich_chuyen(arr):

    shift = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            shift += 1
            j -= 1

        arr[j + 1] = key

    return shift


arr = [3, 2, 1]
print(dem_dich_chuyen(arr))