from collections import deque


class NganXep:

    def __init__(self):
        self.hang_doi_1 = deque()
        self.hang_doi_2 = deque()

    def day(self, gia_tri):
        self.hang_doi_1.append(gia_tri)

    def lay_ra(self):

        if len(self.hang_doi_1) == 0:
            return "Rỗng"

        while len(self.hang_doi_1) > 1:
            self.hang_doi_2.append(
                self.hang_doi_1.popleft()
            )

        ket_qua = self.hang_doi_1.popleft()

        self.hang_doi_1, self.hang_doi_2 = (
            self.hang_doi_2,
            self.hang_doi_1
        )

        return ket_qua


ngan_xep = NganXep()

ngan_xep.day(1)
ngan_xep.day(2)
ngan_xep.day(3)

print(ngan_xep.lay_ra())