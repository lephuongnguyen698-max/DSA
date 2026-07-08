def he_so_tai(so_phan_tu, kich_thuoc):
    return so_phan_tu / kich_thuoc

so_phan_tu = 8
kich_thuoc = 10

if he_so_tai(so_phan_tu, kich_thuoc) > 0.75:
    kich_thuoc *= 2
    
print("Kich thuc moi: ", kich_thuoc)