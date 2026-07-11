def dem_mang_con(ds, muc_tieu):
    bang_bam = {0: 1}

    tong = 0
    dem = 0

    for gia_tri in ds:
        tong += gia_tri

        if tong - muc_tieu in bang_bam:
            dem += bang_bam[tong - muc_tieu]

        if tong in bang_bam:
            bang_bam[tong] += 1
        else:
            bang_bam[tong] = 1

    return dem


ds = [3, 4, 7, 2, -3, 1, 4, 2]
muc_tieu = 7

print("Mảng:", ds)
print("Mục tiêu:", muc_tieu)
print("Số mảng con có tổng bằng", muc_tieu, "là:", dem_mang_con(ds, muc_tieu))