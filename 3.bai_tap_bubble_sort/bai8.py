def is_sorted_after_k_passes(a, k):
    n = len(a)

    for i in range(k):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a == sorted(a)


a = [3, 2, 1]
k = 1

print(is_sorted_after_k_passes(a, k))