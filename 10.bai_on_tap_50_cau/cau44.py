def two_sum(arr, target):
    hash_map = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in hash_map:
            return (hash_map[complement], i)
        hash_map[num] = i
    return None

print(two_sum([2, 7, 11], 9))