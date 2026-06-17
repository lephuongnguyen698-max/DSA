def so_sanh_cach_chen(arr):

    compare_right = 0
    compare_left = 0

    for i in range(1, len(arr)):
        j = i - 1

        while j >= 0:
            compare_right += 1
            j -= 1

    for i in range(1, len(arr)):
        j = 0

        while j < i:
            compare_left += 1
            j += 1

    print("Right to Left =", compare_right)
    print("Left to Right =", compare_left)


arr = [1, 2, 4, 3, 5]

so_sanh_cach_chen(arr)