m, n = map(int, input().split())

a = []
for _ in range(m):
    a.append(list(map(int, input().split())))

x = int(input())

l, r = 0, m * n - 1

while l <= r:
    mid = (l + r) // 2

    row = mid // n
    col = mid % n

    if a[row][col] == x:
        print("true")
        break
    elif a[row][col] < x:
        l = mid + 1
    else:
        r = mid - 1
else:
    print("false")