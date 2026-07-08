may_chu = ["A", "B", "C"]

du_lieu = ["K1", "K2", "K3", "K4"]

for khoa in du_lieu:

    vi_tri = hash(khoa) % len(may_chu)

    print(khoa, "->", may_chu[vi_tri])