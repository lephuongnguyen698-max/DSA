n = int(input())
a = list(map(int, input().split()))
x = int(input())

l, r = 0, n

while l < r:
    mid = (l + r) // 2

    if a[mid] < x:
        l = mid + 1
    else:
        r = mid

print(l)