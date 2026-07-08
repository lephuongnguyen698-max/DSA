def bam_cap(a, b):

    return hash(a) ^ hash(b)


print(bam_cap(5, 8))