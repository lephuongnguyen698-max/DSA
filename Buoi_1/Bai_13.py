def tim_kiem_chuoi(a, x):
    for i in range (0, len(a)):
        if a[i].lower() == x.lower():
            return i
    return -1

a =  ["An", "Bình", "Châu"]
x = 'BìNh'
print(tim_kiem_chuoi(a,x))