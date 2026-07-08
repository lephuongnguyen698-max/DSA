def phan_tich_hieu_nang(arr):

    compare = 0
    shift = 0

    nums = arr.copy()

    for i in range(1, len(nums)):

        key = nums[i]

        j = i - 1

        while j >= 0:

            compare += 1

            if nums[j] > key:

                nums[j + 1] = nums[j]

                shift += 1

                j -= 1

            else:
                break

        nums[j + 1] = key

    print("So lan so sanh =", compare)
    print("So lan shift =", shift)
    print("Mang sau sap xep =", nums)


best_case = [1, 2, 3, 4, 5]
average_case = [3, 1, 4, 5, 2]
worst_case = [5, 4, 3, 2, 1]

print(phan_tich_hieu_nang(best_case))
print(phan_tich_hieu_nang(average_case))
print(phan_tich_hieu_nang(worst_case))