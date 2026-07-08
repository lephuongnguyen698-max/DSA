n = int(input())
a = list(map(int, input().split()))
x = int(input())

left = 0
right = n - 1
ans = -1

while left <= right:
    mid = (left + right) // 2

    if a[mid] == x:
        ans = mid
        right = mid - 1
    elif a[mid] < x:
        left = mid + 1
    else:
        right = mid - 1

print(ans)