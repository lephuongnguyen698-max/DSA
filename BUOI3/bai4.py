def bubble_sort_count_swaps(a):
    n = len(a)
    count = 0

    for i in range(n):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                count += 1

    return count


a = [3, 2, 1]
print(bubble_sort_count_swaps(a))