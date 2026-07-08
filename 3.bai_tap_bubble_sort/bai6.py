def last_element_after_one_pass(a):
    n = len(a)

    for i in range(n - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]

    return a[n - 1]


a = [4, 2, 7, 1, 3]
print(last_element_after_one_pass(a))