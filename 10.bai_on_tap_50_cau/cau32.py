def remove_if_even(arr):
    write_ptr = 0
    
    for read_ptr in range(len(arr)):
        if arr[read_ptr] % 2 != 0:
            arr[write_ptr] = arr[read_ptr]
            write_ptr += 1
            
    del arr[write_ptr:]
    return arr

print(remove_if_even([1, 2, 3, 4]))