def two_sum(mang, muc_tieu):

    da_gap = {}

    for i, so in enumerate(mang):

        if muc_tieu - so in da_gap:
            return da_gap[muc_tieu - so], i

        da_gap[so] = i


print(two_sum([2, 7, 11], 9))