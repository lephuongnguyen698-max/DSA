class NganXepMin:

    def __init__(self):
        self.mang = []
        self.ngan_xep_min = []

    def day(self, gia_tri):

        self.mang.append(gia_tri)

        if (len(self.ngan_xep_min) == 0 or gia_tri <= self.ngan_xep_min[-1]):
            self.ngan_xep_min.append(gia_tri)

    def lay_ra(self):

        if len(self.mang) == 0:
            return "Ngăn xếp rỗng"

        gia_tri = self.mang.pop()

        if gia_tri == self.ngan_xep_min[-1]:
            self.ngan_xep_min.pop()

        return gia_tri

    def lay_nho_nhat(self):

        if len(self.ngan_xep_min) == 0:
            return "Ngăn xếp rỗng"

        return self.ngan_xep_min[-1]

    def hien_thi(self):
        print(self.mang)

ngan_xep = NganXepMin()

ngan_xep.day(5)
ngan_xep.day(3)
ngan_xep.day(7)
ngan_xep.day(2)

print("Stack:")
ngan_xep.hien_thi()

print("Nhỏ nhất:", ngan_xep.lay_nho_nhat())
print("Lấy:", ngan_xep.lay_ra())
print("Nhỏ nhất:", ngan_xep.lay_nho_nhat())