def phan_tu_lon_hon_tiep_theo(mang):

    ket_qua = [-1] * len(mang)

    ngan_xep = []

    for i in range(len(mang)):

        while (
            ngan_xep
            and mang[i] > mang[ngan_xep[-1]]
        ):

            vi_tri = ngan_xep.pop()

            ket_qua[vi_tri] = mang[i]

        ngan_xep.append(i)

    return ket_qua


a = [2, 1, 3]

print(phan_tu_lon_hon_tiep_theo(a))