def reverse_subbarray(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def rotate_right(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    k = k % n
    
    reverse_subbarray(arr, 0, n - 1)
    reverse_subbarray(arr, 0, k - 1)
    reverse_subbarray(arr, k, n - 1)
    return arr

print(rotate_right([1, 2, 3, 4, 5], 2))