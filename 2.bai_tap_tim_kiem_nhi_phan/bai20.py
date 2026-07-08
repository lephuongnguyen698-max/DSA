n = int(input())
p = list(map(int, input().split()))
m = int(input())

l, r = max(p), sum(p)

while l < r:
    mid = (l + r) // 2

    students = 1
    pages = 0

    for x in p:
        if pages + x > mid:
            students += 1
            pages = x
        else:
            pages += x

    if students <= m:
        r = mid
    else:
        l = mid + 1

print(l)