class HangDoi:

    def __init__(self):
        self.ngan_xep_vao = []
        self.ngan_xep_ra = []

    def them(self, x):

        self.ngan_xep_vao.append(x)

    def lay_ra(self):

        if len(self.ngan_xep_ra) == 0:

            while self.ngan_xep_vao:

                self.ngan_xep_ra.append(self.ngan_xep_vao.pop())

        if len(self.ngan_xep_ra) == 0:
            return None

        return self.ngan_xep_ra.pop()


q = HangDoi()

q.them(10)

q.them(20)

print( q.lay_ra())