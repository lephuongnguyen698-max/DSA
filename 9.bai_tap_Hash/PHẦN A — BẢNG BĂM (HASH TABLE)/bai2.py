class BangBamDo:
    
    def __init__(self, kich_thuoc = 10):
        self.bang = [None] * kich_thuoc
        
    def bam(self, khoa):
        return hash(khoa) % len(self.bang)
    
    def them(self, khoa, gia_tri):
        i = self.bam(khoa)
        
        while self.bang[i]:
            i = (i + 1) % len(self.bang)
            
        self.bang[i] = (khoa, gia_tri)
        
    def lay(self, khoa):
        
        for x in self.bang:
            if x and x [0] == khoa:
                return x[1]
            
        return None
    
bang = BangBamDo()
bang.them("a", 5)

print(bang.lay("a"))
            