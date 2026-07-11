def ngay_am_hon(ds_nhiet_do):
    ngan_xep = []
    ket_qua = [0] * len(ds_nhiet_do)

    for i in range(len(ds_nhiet_do)):
        while ngan_xep and ds_nhiet_do[i] > ds_nhiet_do[ngan_xep[-1]]:
            
            vi_tri = ngan_xep.pop()
            ket_qua[vi_tri] = i - vi_tri

        ngan_xep.append(i)

    return ket_qua


ds_nhiet_do = [73, 74, 75, 71, 69, 72, 76, 73]

print("Nhiệt độ:", ds_nhiet_do)
print("Kết quả:", ngay_am_hon(ds_nhiet_do))