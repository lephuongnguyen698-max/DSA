def dem_tan_suat(mang):

    dem = {}

    for x in mang:
        dem[x] = dem.get(x, 0) + 1

    return dem


print(dem_tan_suat(["a", "b", "a", "c", "a"]))