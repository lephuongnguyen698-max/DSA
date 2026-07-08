def bubble_sort_characters(a):
    n = len(a)

    for i in range(n):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a


a = ['d', 'a', 'c', 'b']
print(bubble_sort_characters(a))