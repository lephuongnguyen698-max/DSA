print("Nhap n:")
n = int(input())

print("Nhap mang:")
a = list(map(int, input().split()))

print("Nhap x:")
x = int(input())
left = 0
right = n - 1

while left <= right:
    mid = (left + right) // 2

    if a[mid] == x:
        print(mid)
        break
    elif a[mid] < x:
        left = mid + 1
    else:
        right = mid - 1
else:
    print(-1)