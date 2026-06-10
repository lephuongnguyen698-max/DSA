def min_passes(start, target):
    a = start.copy()
    n = len(a)

    for passes in range(n):
        if a == target:
            return passes

        for j in range(n - 1 - passes):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return -1


start = [4, 3, 2, 1]
target = [3, 2, 1, 4]

print(min_passes(start, target))