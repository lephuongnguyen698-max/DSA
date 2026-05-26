def tim_max(a):
    max = a[0]
    for i in range (1, len(a)):
        if a[i] > max:
            max = a[i]
            print(f"giá trị max: {max}, ở vị trí {i}")

a = [4, 1, 4, 9, 4]
tim_max(a)