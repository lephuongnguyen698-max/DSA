def tim_kiem_ma_tran(M, x):
    for i in range(len(M)):          # duyệt từng dòng
        for j in range(len(M[i])):   # duyệt từng cột
            if M[i][j] == x:
                return (i, j)        # trả về vị trí đầu tiên tìm thấy
    return (-1, -1)                  # không tìm thấy

# Ví dụ
M = [
    [5, 8, 1],
    [3, 9, 7],
    [2, 6, 4]
]
x = 9
print(tim_kiem_ma_tran(M, x))