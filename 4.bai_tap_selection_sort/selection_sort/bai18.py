def so_sanh_swap(arr):
    selection_swap = 0
    
    nums = arr.copy()

    for i in range(len(nums)):
        min_index = i
        
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
                
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]
            
            selection_swap += 1
            
    print("Selection swap = ", selection_swap)
    
arr = [5, 2, 4, 1, 3]
so_sanh_swap(arr)  