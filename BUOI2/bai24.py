n = int(input())
x = list(map(float, input().split()))
k = int(input())

l = 0.0
r = x[-1] - x[0]

while r - l > 1e-6:
    mid = (l + r) / 2

    need = 0

    for i in range(n - 1):
        gap = x[i + 1] - x[i]
        need += int(gap / mid)

        if gap % mid == 0:
            need -= 1

    if need <= k:
        r = mid
    else:
        l = mid

print(f"{r:.6f}")