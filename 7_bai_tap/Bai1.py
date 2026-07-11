def dem_so_xe(ds_khoi_luong, tai_trong):
    so_xe = 1
    tong_hien_tai = 0

    for khoi_luong in ds_khoi_luong:
        if tong_hien_tai + khoi_luong <= tai_trong:
            tong_hien_tai += khoi_luong
        else:
            so_xe += 1
            tong_hien_tai = khoi_luong

    return so_xe


def tim_tai_trong_nho_nhat(ds_khoi_luong, so_xe):
    trai = max(ds_khoi_luong)
    phai = sum(ds_khoi_luong)

    while trai < phai:
        giua = (trai + phai) // 2

        if dem_so_xe(ds_khoi_luong, giua) <= so_xe:
            phai = giua
        else:
            trai = giua + 1

    return trai


def chia_hang(ds_khoi_luong, tai_trong):
    ket_qua = []
    xe_hien_tai = []
    tong = 0

    for khoi_luong in ds_khoi_luong:
        if tong + khoi_luong <= tai_trong:
            xe_hien_tai.append(khoi_luong)
            tong += khoi_luong
        else:
            ket_qua.append(xe_hien_tai)
            xe_hien_tai = [khoi_luong]
            tong = khoi_luong

    ket_qua.append(xe_hien_tai)
    return ket_qua

ds_khoi_luong = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
so_xe = 5

tai_trong = tim_tai_trong_nho_nhat(ds_khoi_luong, so_xe)

print("Tải trọng nhỏ nhất:", tai_trong)

danh_sach_xe = chia_hang(ds_khoi_luong, tai_trong)

for i in range(len(danh_sach_xe)):
    print(f"Xe {i+1}: {danh_sach_xe[i]} - Tổng = {sum(danh_sach_xe[i])}")