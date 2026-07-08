def dfs(do_thi, bat_dau):

    da_tham = set()

    ngan_xep = [bat_dau]

    while ngan_xep:

        dinh = ngan_xep.pop()

        if dinh not in da_tham:

            print(dinh, end=" ")

            da_tham.add(dinh)

            for ke in reversed(do_thi[dinh]):
                ngan_xep.append(ke)


do_thi = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}

dfs(do_thi, "A")