def bubble_sort(a):
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

    return a, passes


def cocktail_shaker_sort(a):
    start = 0
    end = len(a) - 1
    swapped = True
    passes = 0

    while swapped:
        swapped = False

        # trái -> phải
        for i in range(start, end):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        passes += 1

        if not swapped:
            break

        swapped = False
        end -= 1

        # phải -> trái
        for i in range(end - 1, start - 1, -1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        passes += 1
        start += 1

    return a, passes


a = [5, 1, 4, 2, 8]

b1, p1 = bubble_sort(a.copy())
b2, p2 = cocktail_shaker_sort(a.copy())

print("Bubble Sort:", b1, "- So luot:", p1)
print("Cocktail Shaker Sort:", b2, "- So luot:", p2)