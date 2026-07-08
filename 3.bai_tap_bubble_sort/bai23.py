def analyze_bubble_sort(a):
    n = len(a)
    comparisons = 0
    swaps = 0

    for i in range(n):
        swapped = False

        for j in range(n - 1 - i):
            comparisons += 1

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True

        if not swapped:
            break

    return comparisons, swaps


print(analyze_bubble_sort([1, 2, 3, 4]))
print(analyze_bubble_sort([4, 3, 2, 1]))
print(analyze_bubble_sort([3, 1, 4, 2]))