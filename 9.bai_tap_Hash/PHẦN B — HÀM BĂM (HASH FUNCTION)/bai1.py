def ham_bam(khoa, kich_thuoc):
    return khoa % kich_thuoc

kich_thuoc = 10
for khoa in [15, 27, 37, 48]:
    print(khoa, "->", ham_bam(khoa, kich_thuoc))