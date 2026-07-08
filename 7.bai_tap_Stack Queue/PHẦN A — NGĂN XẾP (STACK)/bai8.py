def tinh_hau_to(bieu_thuc):

    ngan_xep = []

    for phan_tu in bieu_thuc.split():

        if phan_tu.lstrip("-").isdigit():
            ngan_xep.append(int(phan_tu))

        else:

            so_2 = ngan_xep.pop()
            so_1 = ngan_xep.pop()

            if phan_tu == "+":
                ket_qua = so_1 + so_2

            elif phan_tu == "-":
                ket_qua = so_1 - so_2

            elif phan_tu == "*":
                ket_qua = so_1 * so_2

            elif phan_tu == "/":
                ket_qua = so_1 / so_2

            ngan_xep.append(ket_qua)

    return ngan_xep.pop()


# Chạy thử
bieu_thuc = "3 4 + 2 *"

print("Kết quả:", tinh_hau_to(bieu_thuc))