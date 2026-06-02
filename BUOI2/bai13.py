n = int(input())
a = list(map(int, input().split()))

l, r = 0, n - 1

while l < r:
    mid = (l + r) // 2

    if mid % 2 == 1:
        mid -= 1

    if a[mid] == a[mid + 1]:
        l = mid + 2
    else:
        r = mid

print(a[l])