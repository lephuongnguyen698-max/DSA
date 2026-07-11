class Nut:
    def __init__(self, du_lieu):
        self.du_lieu = du_lieu
        self.ke_tiep = None


def tim_diem_bat_dau_chu_trinh(dau):
    rua = dau
    tho = dau

    while tho and tho.ke_tiep:
        rua = rua.ke_tiep
        tho = tho.ke_tiep.ke_tiep

        if rua == tho:
            rua = dau

            while rua != tho:
                rua = rua.ke_tiep
                tho = tho.ke_tiep

            return rua

    return None


nut1 = Nut(1)
nut2 = Nut(2)
nut3 = Nut(3)
nut4 = Nut(4)
nut5 = Nut(5)

nut1.ke_tiep = nut2
nut2.ke_tiep = nut3
nut3.ke_tiep = nut4
nut4.ke_tiep = nut5
nut5.ke_tiep = nut3

ket_qua = tim_diem_bat_dau_chu_trinh(nut1)

if ket_qua:
    print("Chu trình bắt đầu tại nút:", ket_qua.du_lieu)
else:
    print("Không có chu trình.")