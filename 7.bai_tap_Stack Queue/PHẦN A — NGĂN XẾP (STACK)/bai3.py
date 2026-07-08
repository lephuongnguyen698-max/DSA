def mo_phong_ngan_xep(danh_sach_lenh):
    ngan_xep = []
    
    for lenh in danh_sach_lenh:
        
        if lenh.startswith("push"):
            gia_tri = int(lenh.split()[1])
            ngan_xep.append(gia_tri)
            
        elif lenh == "pop":
            if len(ngan_xep) == 0:
                print("ngan xep rong")
            else:
                print("Lay ra: ", ngan_xep.pop())
            
    print("Ngan xep cuoi: ", ngan_xep)
    
cac_lenh = [
    "push 5",
    "push 7",
    "push 10",
    "pop",
    "push 20",
    "pop"
]    

mo_phong_ngan_xep(cac_lenh)