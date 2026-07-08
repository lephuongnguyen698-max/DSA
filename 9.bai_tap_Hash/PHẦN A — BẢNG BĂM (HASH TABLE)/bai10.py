def khong_lap_dau_tien(chuoi):

    dem = {}

    for ky_tu in chuoi:
        dem[ky_tu] = dem.get(ky_tu, 0) + 1

    for ky_tu in chuoi:
        if dem[ky_tu] == 1:
            return ky_tu


print(khong_lap_dau_tien("leetcode"))