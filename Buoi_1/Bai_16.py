def tim_gan_nhat(a, x):
    gan_nhat = a[0]
    vi_tri = 0
    for i in range(1, len(a)):
        if abs(a[i] - x) < abs(gan_nhat - x):
            gan_nhat = a[i]
            vi_tri = i
    return gan_nhat, vi_tri


a = [10, 22, 28, 29, 40]
x = 26
gia_tri, vi_tri = tim_gan_nhat(a, x)
print("Giá trị gần nhất:", gia_tri)
print("Vị trí:", vi_tri)