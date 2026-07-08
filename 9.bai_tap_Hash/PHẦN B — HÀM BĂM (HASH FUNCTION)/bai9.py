import random

def ham_bam(k, a, b, p, m):

    return ((a * k + b) % p) % m


a = random.randint(1, 10)
b = random.randint(0, 10)

print(ham_bam(50, a, b, 101, 10))