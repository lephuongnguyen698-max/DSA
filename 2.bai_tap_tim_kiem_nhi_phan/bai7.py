n = int(input())
a = list(map(int, input().split()))
x = int(input())

left, right = 0, n - 1
ans = n

while left <= right:
    mid = (left + right) // 2

    if a[mid] > x:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)