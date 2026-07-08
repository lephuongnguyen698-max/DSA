du_lieu = [10, 20, 30, 40]

kich_thuoc = 10

for x in du_lieu:

    print(x, "->", x % kich_thuoc)

print("Nhiều khóa vào cùng bucket sẽ làm giảm hiệu năng.")