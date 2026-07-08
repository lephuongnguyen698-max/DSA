def mo_phong_hang_doi(cac_lenh):

    hang_doi = []

    for lenh in cac_lenh:

        if lenh.startswith("enq"):

            gia_tri = int(lenh.split()[1])
            hang_doi.append(gia_tri)

        elif lenh == "deq":

            if len(hang_doi) == 0:
                print("Rỗng")

            else:
                print(hang_doi.pop(0))

    print(hang_doi)


cac_lenh = [
    "enq 5",
    "enq 7",
    "deq"
]

mo_phong_hang_doi(cac_lenh)