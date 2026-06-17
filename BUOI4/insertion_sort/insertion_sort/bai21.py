def dem_shift_lon(arr):

    def merge_count(left, right):

        result = []

        i = 0
        j = 0

        count = 0

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                count += len(left) - i
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result, count

    def merge_sort(nums):

        if len(nums) <= 1:
            return nums, 0

        mid = len(nums) // 2

        left, count_left = merge_sort(nums[:mid])
        right, count_right = merge_sort(nums[mid:])

        merged, count_merge = merge_count(left, right)

        return merged, count_left + count_right + count_merge

    _, shift = merge_sort(arr)

    return shift


arr = [2, 4, 1, 3]

print("Tong shift =", dem_shift_lon(arr))