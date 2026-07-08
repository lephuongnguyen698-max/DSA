def bfs(do_thi, bat_dau):

    da_tham = []
    hang_doi = [bat_dau]

    while hang_doi:

        dinh = hang_doi.pop(0)

        if dinh not in da_tham:

            print(dinh, end=" ")

            da_tham.append(dinh)

            for ke in do_thi[dinh]:

                hang_doi.append(ke)


do_thi = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}

bfs(do_thi, "A")