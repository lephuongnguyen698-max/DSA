class HangDoiUuTien:

    def __init__(self):
        self.mang = []

    def them(self, gia_tri):

        self.mang.append( gia_tri)

        self.mang.sort(reverse=True)

    def lay_ra(self):

        if len(self.mang) == 0:
            return "Rỗng"

        return self.mang.pop(0)


q = HangDoiUuTien()

q.them(4)
q.them(9)
q.them(2)

print(
    q.lay_ra()
)