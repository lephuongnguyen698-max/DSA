def tim_vi_tri(arr, left, right, key):

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] > key:
            right = mid - 1
        else:
            left = mid + 1

    return left


def binary_insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        pos = tim_vi_tri(arr, 0, i - 1, key)

        j = i - 1

        while j >= pos:
            arr[j + 1] = arr[j]
            j -= 1

        arr[pos] = key

    return arr


arr = [5, 2, 4, 6, 1, 3]

print(binary_insertion_sort(arr))