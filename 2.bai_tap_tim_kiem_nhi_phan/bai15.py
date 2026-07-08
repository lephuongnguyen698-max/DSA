n = int(input())
a = list(map(int, input().split()))
k = int(input())
x = int(input())

l, r = 0, n - k

while l < r:
    mid = (l + r) // 2

    if x - a[mid] > a[mid + k] - x:
        l = mid + 1
    else:
        r = mid

print(*a[l:l + k])