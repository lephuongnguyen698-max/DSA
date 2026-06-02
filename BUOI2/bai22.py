m = int(input())
a = list(map(int, input().split()))

n = int(input())
b = list(map(int, input().split()))

if m > n:
    a, b = b, a
    m, n = n, m

l, r = 0, m

while l <= r:
    i = (l + r) // 2
    j = (m + n + 1) // 2 - i

    a_left = float('-inf') if i == 0 else a[i - 1]
    a_right = float('inf') if i == m else a[i]

    b_left = float('-inf') if j == 0 else b[j - 1]
    b_right = float('inf') if j == n else b[j]

    if a_left <= b_right and b_left <= a_right:
        if (m + n) % 2 == 1:
            print(float(max(a_left, b_left)))
        else:
            ans = (max(a_left, b_left) + min(a_right, b_right)) / 2
            print(ans)
        break

    elif a_left > b_right:
        r = i - 1
    else:
        l = i + 1