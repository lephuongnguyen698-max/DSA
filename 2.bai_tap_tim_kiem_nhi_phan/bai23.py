n = int(input())

a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

k = int(input())

l = a[0][0]
r = a[n - 1][n - 1]

while l < r:
    mid = (l + r) // 2

    count = 0
    col = n - 1

    for row in range(n):
        while col >= 0 and a[row][col] > mid:
            col -= 1
        count += col + 1

    if count < k:
        l = mid + 1
    else:
        r = mid

print(l)