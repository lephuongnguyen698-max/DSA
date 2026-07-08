def chen_phan_tu(arr, x):
    arr.append(x)

    i = len(arr) - 2

    while i >= 0 and arr[i] > x:
        arr[i + 1] = arr[i]
        i -= 1

    arr[i + 1] = x

    return arr


arr = [1, 3, 5, 7]
print(chen_phan_tu(arr, 4))