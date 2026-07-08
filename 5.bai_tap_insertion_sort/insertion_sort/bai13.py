def kiem_tra_on_dinh(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j][0] > key[0]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


arr = [(2, 'a'), (1, 'b'), (2, 'c')]

print(kiem_tra_on_dinh(arr))