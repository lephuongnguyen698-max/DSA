class BangBam:

    def __init__(self, kich_thuoc=10):
        self.bang = [[] for _ in range(kich_thuoc)]

    def bam(self, khoa):
        return hash(khoa) % len(self.bang)

    def them(self, khoa, gia_tri):

        o = self.bang[self.bam(khoa)]

        for i in range(len(o)):

            if o[i][0] == khoa:
                o[i] = (khoa, gia_tri)
                return

        o.append((khoa, gia_tri))


    def lay(self, khoa):

        o = self.bang[self.bam(khoa)]

        for k, v in o:

            if k == khoa:
                return v

        return None


    def xoa(self, khoa):

        o = self.bang[self.bam(khoa)]

        for i in range(len(o)):

            if o[i][0] == khoa:
                o.pop(i)
                return True

        return False



# Test
bang = BangBam()

bang.them("a", 10)
bang.them("b", 20)

print(bang.lay("a"))

bang.xoa("b")