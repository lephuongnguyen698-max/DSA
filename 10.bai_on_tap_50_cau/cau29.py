from collections import deque

def max_sliding_window(arr, k):
    n = len(arr)
    if n == 0 or k == 0:
        return []
    
    result = []
    dq = deque()
    
    for i in range(n):
        if dq and dq[0] < i - k + 1:
            dq.popleft()
            
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
            
        dq.append(i)
        
        if i >= k - 1:
            result.append(arr[dq[0]])
            
    return result

print(max_sliding_window([1, 3, -1, -3, 5, 3], 3))