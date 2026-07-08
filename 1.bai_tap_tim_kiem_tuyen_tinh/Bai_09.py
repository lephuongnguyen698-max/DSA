def tim_tat_ca(a, x):
    b = []
    dem = 0
    for i in range(0, len(a)):
        if a[i] == x:
            b += str(i)
            dem += 1
    return b

a = [4, 1, 4, 9, 4]
x = 5
print(tim_tat_ca(a,x))