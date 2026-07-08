class HangDoi:

    def __init__(self):
        self.mang = []

    def them(self, gia_tri):
        self.mang.append(gia_tri)

    def lay_ra(self):

        if len(self.mang) == 0:
            return "Hàng đợi rỗng"

        return self.mang.pop(0)

    def xem_dau(self):

        if len(self.mang) == 0:
            return "Hàng đợi rỗng"

        return self.mang[0]

    def kiem_tra_rong(self):
        return len(self.mang) == 0


hang_doi = HangDoi()

hang_doi.them(1)
hang_doi.them(2)
hang_doi.them(3)

print(hang_doi.lay_ra())