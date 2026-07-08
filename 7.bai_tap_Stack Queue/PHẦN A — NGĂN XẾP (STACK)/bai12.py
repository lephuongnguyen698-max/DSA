def hinh_chu_nhat_lon_nhat(chieu_cao):

    ngan_xep = []

    lon_nhat = 0

    i = 0

    while i < len(chieu_cao):

        if (
            not ngan_xep
            or chieu_cao[i]
            >= chieu_cao[ngan_xep[-1]]
        ):
            ngan_xep.append(i)
            i += 1

        else:

            dinh = ngan_xep.pop()

            rong = (
                i
                if not ngan_xep
                else i - ngan_xep[-1] - 1
            )

            lon_nhat = max(
                lon_nhat,
                chieu_cao[dinh] * rong
            )

    while ngan_xep:

        dinh = ngan_xep.pop()

        rong = (
            i
            if not ngan_xep
            else i - ngan_xep[-1] - 1
        )

        lon_nhat = max(
            lon_nhat,
            chieu_cao[dinh] * rong
        )

    return lon_nhat


h = [2, 1, 5, 6, 2, 3]

print(hinh_chu_nhat_lon_nhat(h))