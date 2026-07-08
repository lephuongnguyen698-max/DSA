class HangDoi:

    def __init__(self):
        self.ngan_xep_vao = []
        self.ngan_xep_ra = []

    def them(self, gia_tri):

        self.ngan_xep_vao.append(gia_tri)

    def lay_ra(self):

        if len(self.ngan_xep_ra) == 0:

            while self.ngan_xep_vao:

                self.ngan_xep_ra.append(self.ngan_xep_vao.pop())

        if len(self.ngan_xep_ra) == 0:
            return "Rỗng"

        return self.ngan_xep_ra.pop()


q = HangDoi()

q.them(1)
q.them(2)
q.them(3)

print(q.lay_ra())