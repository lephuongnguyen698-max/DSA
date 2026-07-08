def subarray_sum_equals_k(arr, k):
    count = 0
    prefix_sum = 0
    hash_map = {0: 1}
    
    for num in arr:
        prefix_sum += num
        if (prefix_sum - k) in hash_map:
            count += hash_map[prefix_sum - k]
        hash_map[prefix_sum] = hash_map.get(prefix_sum, 0) + 1
        
    return count

print(subarray_sum_equals_k([1, 1, 1], 2))