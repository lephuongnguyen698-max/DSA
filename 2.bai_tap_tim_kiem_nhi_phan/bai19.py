n = int(input())
x = list(map(int, input().split()))
c = int(input())

x.sort()

l, r = 1, x[-1] - x[0]
ans = 0

while l <= r:
    mid = (l + r) // 2

    cnt = 1
    last = x[0]

    for i in range(1, n):
        if x[i] - last >= mid:
            cnt += 1
            last = x[i]

    if cnt >= c:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)