def bubble_sort_students(a):
    n = len(a)

    for i in range(n):
        for j in range(n - 1 - i):

            # Điểm giảm dần
            if a[j][1] < a[j + 1][1]:
                a[j], a[j + 1] = a[j + 1], a[j]

            # Nếu điểm bằng nhau -> tên tăng dần
            elif a[j][1] == a[j + 1][1]:
                if a[j][0] > a[j + 1][0]:
                    a[j], a[j + 1] = a[j + 1], a[j]

    return a


a = [('An', 8), ('Ba', 9), ('Cu', 8)]

print(bubble_sort_students(a))