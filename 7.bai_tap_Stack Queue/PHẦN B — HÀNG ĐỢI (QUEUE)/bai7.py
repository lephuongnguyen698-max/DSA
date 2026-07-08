def dao_nguoc_hang_doi(hang_doi):

    ngan_xep = []

    while hang_doi:

        ngan_xep.append(hang_doi.pop(0))

    while ngan_xep:

        hang_doi.append(ngan_xep.pop())

    return hang_doi


q = [1, 2, 3]

print(dao_nguoc_hang_doi(q))