class HangDoiCoDinh:

    def __init__(self, suc_chua):
        self.mang = []
        self.suc_chua = suc_chua

    def them(self, gia_tri):

        if len(self.mang) >= self.suc_chua:
            print("Đầy")
            return

        self.mang.append(gia_tri)

    def lay_ra(self):

        if len(self.mang) == 0:
            print("Rỗng")
            return

        return self.mang.pop(0)

    def dem(self):
        return len(self.mang)


q = HangDoiCoDinh(3)

q.them(1)
q.them(2)
q.them(3)
q.them(4)

print(q.dem())