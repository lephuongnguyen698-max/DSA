def phan_tich_hieu_nang(arr):

    compare = 0
    swap = 0

    nums = arr.copy()

    for i in range(len(nums)):

        min_index = i

        for j in range(i + 1, len(nums)):

            compare += 1

            if nums[j] < nums[min_index]:
                min_index = j

        if min_index != i:

            nums[i], nums[min_index] = nums[min_index], nums[i]

            swap += 1

    print("So lan so sanh =", compare)
    print("So lan swap =", swap)
    print(nums)


arr = [5, 4, 3, 2, 1]

phan_tich_hieu_nang(arr)