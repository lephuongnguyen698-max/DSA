def dem_va_cham(ds, kich_thuoc):

    bang = {}
    va_cham = 0

    for x in ds:

        chi_so = x % kich_thuoc

        if chi_so in bang:
            va_cham += 1
        else:
            bang[chi_so] = 1

    return va_cham


print(dem_va_cham([12, 22, 32, 15], 10))