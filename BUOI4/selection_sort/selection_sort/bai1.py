def dua_nho_nhat_ve_dau(arr):
    min_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
            
    arr[0], arr[min_index] = arr[min_index], arr[0]
    
    return arr

arr = [4, 2, 7, 1, 3]
print(dua_nho_nhat_ve_dau(arr))