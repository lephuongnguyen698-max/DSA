def tim_so_nguyen_to(a):
    for i in range (0, len(a)):
        dem = 0
        for j in range (1, a[i]+1):
            if a[i] % j == 0:
                dem+=1
        if dem == 2:
            return a[i]
    return -1

a = [4, 6, 9, 7, 11]
print(tim_so_nguyen_to(a))