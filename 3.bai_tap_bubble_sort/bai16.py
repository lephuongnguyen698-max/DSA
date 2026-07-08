def inversion_and_swaps(a):
    n = len(a)

    # Đếm số nghịch thế
    inversions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                inversions += 1

    # Bubble Sort và đếm swap
    swaps = 0
    b = a.copy()

    for i in range(n):
        for j in range(n - 1 - i):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
                swaps += 1

    return inversions, swaps


a = [2, 3, 1]

inv, sw = inversion_and_swaps(a)

print("So nghich the:", inv)
print("So swap:", sw)