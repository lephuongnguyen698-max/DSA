def mang_gan_sap_xep(arr):

    shift = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            shift += 1
            j -= 1

        arr[j + 1] = key

    print("Shift =", shift)

    return arr


arr = [1, 2, 4, 3, 5]

print(mang_gan_sap_xep(arr))