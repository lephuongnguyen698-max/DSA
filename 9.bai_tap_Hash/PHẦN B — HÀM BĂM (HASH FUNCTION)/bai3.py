def polynomial_hash(chuoi, p=31, m=1000000007):

    gia_tri = 0

    for ky_tu in chuoi:
        gia_tri = (gia_tri * p + ord(ky_tu)) % m

    return gia_tri


print(polynomial_hash("hello"))