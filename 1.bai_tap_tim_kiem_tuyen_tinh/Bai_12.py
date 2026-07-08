def tim_max_min(a):
    max = a[0]
    min = a[0]
    vi_tri_max = 0
    vi_tri_min = 0
    for i in range (1, len(a)):
        if a[i] > max:
            max = a[i]
            vi_tri_max = i
        if a[i] < min:
            min = a[i]
            vi_tri_min = i
    print(f"giá trị max: {max} ở vị trí {vi_tri_max}")
    print(f"giá trị max: {min} ở vị trí {vi_tri_min}")
        
a = [4, 1, 4, 9, 4]
tim_max_min(a)