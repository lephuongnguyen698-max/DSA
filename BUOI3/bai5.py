def bubble_sort_count_comparisons(a):
    n = len(a)
    count = 0

    for i in range(n):
        for j in range(n - 1 - i):
            count += 1

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return count


a = [1, 2, 3]
print(bubble_sort_count_comparisons(a))