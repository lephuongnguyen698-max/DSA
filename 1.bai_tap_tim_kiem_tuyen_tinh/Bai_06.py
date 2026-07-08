def linear_search(a, x):
    for i in range(0, len(a)):
        if a[i] == x:
            return i
    return -1

a = [7, 3, 9, 12, 5, 8, 1, 5] 
x = 5
print("vị trí của x ở trong array[] là: " +str(linear_search(a, x)))