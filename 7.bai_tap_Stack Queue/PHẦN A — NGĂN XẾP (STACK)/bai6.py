def kiem_tra_ngoac_can_bang(chuoi):
    
    ngan_xep = []
    cap_ngoac = {
         ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for ky_tu in chuoi:

        if ky_tu in "([{":
            ngan_xep.append(ky_tu)

        elif ky_tu in ")]}":

            if len(ngan_xep) == 0:
                return False

            dinh = ngan_xep.pop()

            if dinh != cap_ngoac[ky_tu]:
                return False

    return len(ngan_xep) == 0


chuoi_1 = "([]{})"
chuoi_2 = "([)]"

print(chuoi_1, "→", kiem_tra_ngoac_can_bang(chuoi_1))
print(chuoi_2, "→", kiem_tra_ngoac_can_bang(chuoi_2))    