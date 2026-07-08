def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

def linh_canh(a, x):
    n = len(a)
    phan_tu_cuoi = a[n - 1]
    a[n - 1] = x
    i = 0
    while a[i] != x:
        i += 1
    a[n - 1] = phan_tu_cuoi
    if i < n - 1 or phan_tu_cuoi == x:
        return i
    return -1

a = [4, 7, 2, 9, 5]
x = int(input("Nhap x: "))

print("Tim kiem thong thuong:")
print(linear_search(a, x))
print("Tim kiem linh canh:")
print(linh_canh(a, x))