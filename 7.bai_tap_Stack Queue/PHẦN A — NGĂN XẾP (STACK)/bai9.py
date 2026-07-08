def do_uu_tien(toan_tu):
    
    if toan_tu in "*/":
        return 2

    if toan_tu in "+-":
        return 1

    return 0

def chuyen_trung_to_sang_hau_to(bieu_thuc):
    ngan_xep =[]
    hau_to = " "
    
    for ky_tu in bieu_thuc:
        
        if ky_tu.isalnum():
            hau_to += ky_tu + " "
            
        elif ky_tu == "(":
            ngan_xep.append(ky_tu)
            
        elif ky_tu == ")":
            
            while ngan_xep and ngan_xep[-1] != "(":
                hau_to += ngan_xep.pop() + " "

            ngan_xep.pop()

        else:

            while (
                ngan_xep
                and do_uu_tien(ngan_xep[-1]) >= do_uu_tien(ky_tu)
            ):
                hau_to += ngan_xep.pop() + " "

            ngan_xep.append(ky_tu)

    while ngan_xep:
        hau_to += ngan_xep.pop() + " "

    return hau_to


bieu_thuc = "a+b*c"
print("Hậu tố:")
print(chuyen_trung_to_sang_hau_to(bieu_thuc))