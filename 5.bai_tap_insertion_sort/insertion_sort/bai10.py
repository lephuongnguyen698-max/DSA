def dem_nghich_the(arr):

    count = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                count += 1

    return count


arr = [2, 4, 1, 3]

print("So nghich the =", dem_nghich_the(arr))