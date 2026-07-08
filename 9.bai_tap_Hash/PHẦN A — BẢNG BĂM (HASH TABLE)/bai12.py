def dem_doan_con(mang, k):

    tong = 0
    dem = 0
    bang_bam = {0: 1}

    for so in mang:

        tong += so

        if tong - k in bang_bam:
            dem += bang_bam[tong - k]

        bang_bam[tong] = bang_bam.get(tong, 0) + 1

    return dem


print(dem_doan_con([1, 1, 1], 2))