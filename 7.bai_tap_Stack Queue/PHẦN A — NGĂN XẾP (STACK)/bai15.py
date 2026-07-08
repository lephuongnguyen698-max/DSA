def sap_xep_ngan_xep(ngan_xep):

    ngan_xep_phu = []

    while ngan_xep:

        tam = ngan_xep.pop()

        while (
            ngan_xep_phu
            and ngan_xep_phu[-1] < tam
        ):
            ngan_xep.append(
                ngan_xep_phu.pop()
            )

        ngan_xep_phu.append(tam)

    while ngan_xep_phu:
        ngan_xep.append(
            ngan_xep_phu.pop()
        )

    return ngan_xep


stack = [3, 1, 2]

print(
    sap_xep_ngan_xep(stack)
)