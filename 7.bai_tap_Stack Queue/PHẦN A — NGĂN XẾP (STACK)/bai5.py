class NganXep:

    def __init__(self):
        self.mang = []

    def day(self, gia_tri):
        self.mang.append(gia_tri)

    def lay_ra(self):
        if len(self.mang) == 0:
            return None
        return self.mang.pop()

    def kiem_tra_rong(self):
        return len(self.mang) == 0

    def hien_thi(self):
        print(self.mang)


def duyet_va_dem(ngan_xep):

    ngan_xep_phu = []
    dem = 0

    print("Phần tử theo LIFO:")

    while not ngan_xep.kiem_tra_rong():

        gia_tri = ngan_xep.lay_ra()

        print(gia_tri)

        ngan_xep_phu.append(gia_tri)

        dem += 1

    while len(ngan_xep_phu) > 0:
        ngan_xep.day(ngan_xep_phu.pop())

    print("Số phần tử:", dem)


ngan_xep = NganXep()

ngan_xep.day(1)
ngan_xep.day(2)
ngan_xep.day(3)

duyet_va_dem(ngan_xep)

print("Stack sau khi khôi phục:")
ngan_xep.hien_thi()