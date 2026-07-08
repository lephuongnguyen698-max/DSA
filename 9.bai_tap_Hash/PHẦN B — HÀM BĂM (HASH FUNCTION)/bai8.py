def thong_ke(ds, kich_thuoc):

    bang = [0] * kich_thuoc

    for x in ds:
        bang[x % kich_thuoc] += 1

    return bang


du_lieu = [12, 15, 22, 31, 42]

print(thong_ke(du_lieu, 5))
print(thong_ke(du_lieu, 7))