def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    p = 31
    mod = 1000000007

    hp = 0
    ht = 0
    power = 1

    for i in range(m - 1):
        power = (power * p) % mod

    for i in range(m):
        hp = (hp * p + ord(pattern[i])) % mod
        ht = (ht * p + ord(text[i])) % mod

    for i in range(n - m + 1):
        if hp == ht:
            if text[i:i + m] == pattern:
                return i

        if i < n - m:
            ht = (ht - ord(text[i]) * power) % mod
            ht = (ht * p + ord(text[i + m])) % mod
            ht %= mod

    return -1

print(rabin_karp("zabcd", "abc"))