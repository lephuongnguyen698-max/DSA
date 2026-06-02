def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    step = 0

    while left <= right:
        step += 1
        mid = (left + right) // 2

        print("Bước", step,
              ": left =", left,
              ", right =", right,
              ", mid =", mid,
              ", arr[mid] =", arr[mid])

        if key == arr[mid]:
            print("Tìm thấy sau", step, "bước")
            return mid

        if key < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    print("Không tìm thấy sau", step, "bước")
    return -1


arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

print("=== Tìm x = 95 ===")
result = binary_search(arr, 95)
print("Kết quả:", result)

print()

print("=== Tìm x = 5 ===")
result = binary_search(arr, 5)
print("Kết quả:", result)