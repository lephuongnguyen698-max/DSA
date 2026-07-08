n = int(input())
a = list(map(int, input().split()))
x = int(input())

left = 0
right = n - 1
first = -1

while left <= right:
    mid = (left + right) // 2

    if a[mid] == x:
        first = mid
        right = mid - 1
    elif a[mid] < x:
        left = mid + 1
    else:
        right = mid - 1

left = 0
right = n - 1
last = -1

while left <= right:
    mid = (left + right) // 2

    if a[mid] == x:
        last = mid
        left = mid + 1
    elif a[mid] < x:
        left = mid + 1
    else:
        right = mid - 1

if first == -1:
    print(0)
else:
    print(last - first + 1)