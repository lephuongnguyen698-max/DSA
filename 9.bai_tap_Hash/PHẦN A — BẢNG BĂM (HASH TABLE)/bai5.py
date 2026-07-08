def nhom_theo_chu_dau(ds):

    ket_qua = {}

    for tu in ds:

        khoa = tu[0]

        if khoa not in ket_qua:
            ket_qua[khoa] = []

        ket_qua[khoa].append(tu)

    return ket_qua


print(nhom_theo_chu_dau(["cam", "ca", "chuoi", "tao"]))