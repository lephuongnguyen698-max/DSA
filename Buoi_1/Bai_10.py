def vi_tri_cuoi_cung(a,x):
    for i in range(len(a)-1, -1, -1):
        if a[i] == x:
            return i
    return -1
    
a = [4, 1, 4, 9, 4]
x = 4
print(vi_tri_cuoi_cung(a,x))