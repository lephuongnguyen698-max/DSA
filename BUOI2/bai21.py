n = int(input())
a = list(map(int, input().split()))
k = int(input())

l, r = max(a), sum(a)

while l < r:
    mid = (l + r) // 2

    parts = 1
    cur = 0

    for x in a:
        if cur + x > mid:
            parts += 1
            cur = x
        else:
            cur += x

    if parts <= k:
        r = mid
    else:
        l = mid + 1

print(l)