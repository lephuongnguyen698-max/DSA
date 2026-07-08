def selection_on_dinh(arr):

    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if arr[j][0] < arr[min_index][0]:
                min_index = j

        key = arr[min_index]

        while min_index > i:
            arr[min_index] = arr[min_index - 1]
            min_index -= 1

        arr[i] = key

    return arr


arr = [(2, 'a'), (2, 'b'), (1, 'c')]

print(selection_on_dinh(arr))