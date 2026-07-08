def tim_sinh_vien(ds, ma_sv):
    for sv in ds:
        if sv["ma_sv"] == ma_sv:
            print("Thông tin sinh viên:")
            print("Mã SV:", sv["ma_sv"])
            print("Họ tên:", sv["ho_ten"])
            print("Điểm trung bình:", sv["dtb"])
            return
    
    print("Không tìm thấy sinh viên có mã", ma_sv)


# Danh sách sinh viên
danh_sach = [
    {"ma_sv": "SV001", "ho_ten": "Nguyen Van A", "dtb": 8.5},
    {"ma_sv": "SV002", "ho_ten": "Tran Thi B", "dtb": 7.8},
    {"ma_sv": "SV003", "ho_ten": "Le Van C", "dtb": 9.1}
]

# Tìm sinh viên
tim_sinh_vien(danh_sach, "SV002")