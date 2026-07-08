def trang_thai_k_buoc(arr, k):

    for i in range(1, k + 1):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


arr = [4, 3, 2, 1]

print(trang_thai_k_buoc(arr, 1))