def day_dai_nhat(mang):

    tap = set(mang)
    lon_nhat = 0

    for so in tap:

        if so - 1 not in tap:

            do_dai = 1

            while so + do_dai in tap:
                do_dai += 1

            lon_nhat = max(lon_nhat, do_dai)

    return lon_nhat


print(day_dai_nhat([100, 4, 200, 1, 3, 2]))