n = int(input())
a = list(map(int, input().split()))

l, r = 0, n - 1

while l < r:
    mid = (l + r) // 2

    if a[mid] > a[r]:
        l = mid + 1
    else:
        r = mid

print(a[l])