def tim_chung(mang_1, mang_2):

    tap = set(mang_1)

    ket_qua = []

    for x in mang_2:

        if x in tap:
            ket_qua.append(x)

    return ket_qua


print(tim_chung([1, 2, 3], [2, 3, 4]))