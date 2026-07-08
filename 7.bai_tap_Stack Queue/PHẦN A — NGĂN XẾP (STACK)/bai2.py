def dao_nguoc_chuoi(chuoi):
    ngan_xep = []
    
    for ky_tu in chuoi:
        ngan_xep.append(ky_tu)
        
    ket_qua = " "
    
    while len(ngan_xep) > 0:
        ket_qua += ngan_xep.pop()
        
    return ket_qua

chuoi = "abc"
print("chuoi ban dau: ", chuoi)
ket_qua = dao_nguoc_chuoi(chuoi)
print("sau khi dao: ", chuoi)