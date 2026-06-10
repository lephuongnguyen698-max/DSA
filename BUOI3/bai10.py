def count_bubble_sort_passes(a):
    n = len(a)
    passes = 0

    for i in range(n):
        swapped = False
        passes += 1

        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True

        if not swapped:
            break

    return passes


a = [2, 1, 3, 4]
print(count_bubble_sort_passes(a))