def hash_tap_hop(ds):

    ket_qua = 0

    for x in ds:
        ket_qua ^= hash(x)

    return ket_qua


print(hash_tap_hop([1, 2, 3]))
print(hash_tap_hop([3, 2, 1]))