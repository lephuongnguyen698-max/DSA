class NganXep:
    
    def __init__(self):
        self.mang = []
        
    def day(self, gia_tri):
        self.mang.append(gia_tri)
        
    def lay_ra(self):
        if self.kiem_tra_rong():
            return "Ngan xep rong"
        return self.mang.pop()
    
    def xem_dinh(self):
        if self.kiem_tra_rong():
            return "Ngan xep rong"
        return self.mang[-1]
    
    def kiem_tra_rong(self):
        return len(self.mang) == 0
    
    def hien_thi(self):
        print(self.mang)
        
ngan_xep = NganXep()

ngan_xep.day(1)
ngan_xep.day(2)
ngan_xep.day(3)
        
print("Ngăn xếp:")
ngan_xep.hien_thi()

print("Lấy ra:", ngan_xep.lay_ra())
print("Đỉnh hiện tại:", ngan_xep.xem_dinh())
print("Rỗng:", ngan_xep.kiem_tra_rong())       