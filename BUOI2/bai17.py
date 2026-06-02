n = int(input())
w = list(map(int, input().split()))
D = int(input())

l, r = max(w), sum(w)

while l < r:
    mid = (l + r) // 2

    days = 1
    cur = 0

    for x in w:
        if cur + x > mid:
            days += 1
            cur = x
        else:
            cur += x

    if days <= D:
        r = mid
    else:
        l = mid + 1

print(l)