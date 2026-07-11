def sap_xep_chen(ds):
    so_lan_dich_chuyen = 0

    for i in range(1, len(ds)):
        gia_tri = ds[i]
        j = i - 1

        while j >= 0 and ds[j] > gia_tri:
            ds[j + 1] = ds[j]
            so_lan_dich_chuyen += 1
            j -= 1

        ds[j + 1] = gia_tri

    return so_lan_dich_chuyen


ds = [5, 2, 4, 6, 1, 3]

print("Mảng ban đầu:", ds)

so_dich_chuyen = sap_xep_chen(ds)

print("Mảng sau khi sắp xếp:", ds)
print("Số lần dịch chuyển:", so_dich_chuyen)