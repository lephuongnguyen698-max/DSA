class NganXep:
    def __init__(self, suc_chua):
        self.mang =[]
        self.suc_chua = suc_chua
        
    def day(self, gia_tri):
        
        if len(self.mang) >= self.suc_chua:
            print("Loi Overflow")
            return 
        
        self.mang.append(gia_tri)
        
    def lay_ra(self):
        
        if len(self.mang) == 0:
            print("Loi Underflow")
            return
        
        return self.mang.pop()
    
    def hien_thi(self):
        print(self.mang)
        
ngan_xep = NganXep(3)

ngan_xep.day(10)
ngan_xep.day(20)
ngan_xep.day(30)
ngan_xep.day(40)  

ngan_xep.hien_thi()

print("Lấy:", ngan_xep.lay_ra())
print("Lấy:", ngan_xep.lay_ra())
print("Lấy:", ngan_xep.lay_ra())

ngan_xep.lay_ra() 
         
            
        
        