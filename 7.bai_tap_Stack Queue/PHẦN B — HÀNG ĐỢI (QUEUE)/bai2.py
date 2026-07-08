class HangDoiVong:

    def __init__(self, suc_chua):

        self.mang = [None] * suc_chua
        self.dau = 0
        self.cuoi = -1
        self.so_luong = 0
        self.suc_chua = suc_chua

    def them(self, gia_tri):

        if self.so_luong == self.suc_chua:
            print("Đầy")
            return

        self.cuoi = (self.cuoi + 1) % self.suc_chua
        self.mang[self.cuoi] = gia_tri
        self.so_luong += 1

    def lay_ra(self):

        if self.so_luong == 0:
            return "Rỗng"

        gia_tri = self.mang[self.dau]
        self.dau = (self.dau + 1) % self.suc_chua
        self.so_luong -= 1
        
        return gia_tri


q = HangDoiVong(4)

q.them(10)
q.them(20)

print(q.lay_ra())