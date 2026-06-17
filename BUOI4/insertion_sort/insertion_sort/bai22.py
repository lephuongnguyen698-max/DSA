def do_lech_k(arr, k):

    shift = 0

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= max(0, i - k) and arr[j] > key:

            arr[j + 1] = arr[j]

            shift += 1

            j -= 1

        arr[j + 1] = key

    print("Shift =", shift)

    return arr


arr = [2, 1, 4, 3, 5]

print(do_lech_k(arr, 2))