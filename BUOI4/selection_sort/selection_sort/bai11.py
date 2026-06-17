def tinh_khong_on_dinh(arr):

    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if arr[j][0] < arr[min_index][0]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [(2, 'a'), (2, 'b'), (1, 'c')]

print(tinh_khong_on_dinh(arr))