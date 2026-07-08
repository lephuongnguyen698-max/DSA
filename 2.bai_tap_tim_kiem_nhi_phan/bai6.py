n, x = map(int, input().split())
a = list(map(int, input().split()))

l, r = 0, n - 1

while l <= r:
    mid = (l + r) // 2
    if a[mid] == x:
        print(mid)
        break
    elif a[mid] < x:
        l = mid + 1
    else:
        r = mid - 1
else:
    print(-1)