n = int(input())
pile = list(map(int, input().split()))
h = int(input())

l, r = 1, max(pile)

while l < r:
    mid = (l + r) // 2

    hours = 0
    for x in pile:
        hours += (x + mid - 1) // mid

    if hours <= h:
        r = mid
    else:
        l = mid + 1

print(l)