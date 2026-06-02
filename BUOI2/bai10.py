n = int(input())
a = list(map(int, input().split()))
x = int(input())

l, r = 0, n - 1

while l <= r:
    mid = (l + r) // 2

    if a[mid] == x:
        print(mid)
        break

    if a[l] <= a[mid]:  # nửa trái đã sắp xếp
        if a[l] <= x < a[mid]:
            r = mid - 1
        else:
            l = mid + 1
    else:  # nửa phải đã sắp xếp
        if a[mid] < x <= a[r]:
            l = mid + 1
        else:
            r = mid - 1
else:
    print(-1)