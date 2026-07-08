class HashSet:

    def __init__(self):
        self.tap = set()

    def them(self, gia_tri):
        self.tap.add(gia_tri)

    def kiem_tra(self, gia_tri):
        return gia_tri in self.tap

    def xoa(self, gia_tri):
        self.tap.discard(gia_tri)


tap = HashSet()

tap.them(1)
tap.them(2)
tap.them(2)

print(tap.kiem_tra(2))

tap.xoa(2)

print(tap.kiem_tra(2))