import math

def ham_bam(k, m):

    A = 0.618

    return math.floor(m * ((k * A) % 1))


print(ham_bam(25, 10))