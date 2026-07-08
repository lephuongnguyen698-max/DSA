def phan_bo(ds, kich_thuoc):

    bang = [0] * kich_thuoc

    for x in ds:
        bang[x % kich_thuoc] += 1

    return bang


du_lieu = [5, 10, 15, 20, 25, 30, 35]

print("m = 16:", phan_bo(du_lieu, 16))
print("m = 17:", phan_bo(du_lieu, 17))