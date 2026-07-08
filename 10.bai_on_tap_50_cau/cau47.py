def polynomial_hash(s, p=31, m=1000000007):
    h = 0
    n = len(s)

    for i in range(n):
        h = (h + ord(s[i]) * (p ** (n - i - 1))) % m

    return h

s = "abc"
print(polynomial_hash(s))