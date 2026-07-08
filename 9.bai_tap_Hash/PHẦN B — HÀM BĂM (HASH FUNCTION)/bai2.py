def ham_bam_chuoi(chuoi, kich_thuoc):

    tong = 0

    for ky_tu in chuoi:
        tong += ord(ky_tu)

    return tong % kich_thuoc


print(ham_bam_chuoi("abc", 10))
print(ham_bam_chuoi("cba", 10))